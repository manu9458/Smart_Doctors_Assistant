import streamlit as st

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Smart Doctor Assistant",
    layout="wide"
)

import os
import traceback
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import google.generativeai as genai

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI


###############################################################
# LOGGING SETUP
###############################################################
LOG_FILE = "app.log"

handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)

logger = logging.getLogger("doctor_app")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)


def log_exception(title, e):
    logger.error(f"{title}: {e}")
    logger.error(traceback.format_exc())
    st.error(f"❌ {title}: {e}")
    st.code(traceback.format_exc())


###############################################################
# REMOVE DUPLICATE CHUNKS
###############################################################
def unique_docs(docs):
    """Remove duplicate evidence based on page content string."""
    seen = set()
    unique = []
    for d in docs:
        text = d.page_content.strip()
        if text not in seen:
            seen.add(text)
            unique.append(d)
    return unique


###############################################################
# CONFIG
###############################################################
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("❌ GOOGLE_API_KEY missing in .env")
    st.stop()

try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    log_exception("Gemini configure failed", e)
    st.stop()

logger.info("Gemini configured successfully.")

EMBED_MODEL = "models/text-embedding-004"
LLM_MODEL = "models/gemini-2.5-flash"
DB_DIR = "chroma_db"


###############################################################
# INIT VECTOR STORE
###############################################################
@st.cache_resource
def load_vector_store():
    try:
        vector = Chroma(
            persist_directory=DB_DIR,
            embedding_function=GoogleGenerativeAIEmbeddings(
                model=EMBED_MODEL,
                google_api_key=GOOGLE_API_KEY
            )
        )
        logger.info("Chroma DB initialized.")
        return vector
    except Exception as e:
        log_exception("ChromaDB init failed", e)
        st.stop()

vector_store = load_vector_store()


###############################################################
# FUNCTIONS
###############################################################
def embed_pdf(pdf_path):
    logger.info(f"Indexing PDF: {pdf_path}")

    try:
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
    except Exception as e:
        log_exception("PDF load failed", e)
        return 0

    try:
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_documents(docs)
        logger.info(f"PDF split into {len(chunks)} chunks.")
    except Exception as e:
        log_exception("Text splitting failed", e)
        return 0

    try:
        vector_store.add_documents(chunks)
        vector_store.persist()
        logger.info("PDF successfully embedded into vector DB.")
        return len(chunks)
    except Exception as e:
        log_exception("Embedding failed", e)
        return 0


def rag_query(query):
    logger.info(f"RAG Query: {query}")

    try:
        retriever = vector_store.as_retriever(search_kwargs={"k": 8})
        docs = retriever.invoke(query)
        docs = unique_docs(docs)   # <-- FIX APPLIED (dedupe evidence)
        logger.info(f"Found {len(docs)} unique evidence chunks.")
    except Exception as e:
        log_exception("Chroma Retrieval Failed", e)
        return None, None

    evidence = "\n\n---\n\n".join([d.page_content for d in docs])

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2
    )

    prompt = f"""
Summarize the following medical evidence:

User Query: {query}

Evidence:
{evidence}
"""

    try:
        response = llm.invoke(prompt)
        logger.info("RAG Summary generated.")
        return response.content, docs
    except Exception as e:
        log_exception("Gemini RAG Summary Failed", e)
        return None, docs


def symptom_analysis(symptoms):
    logger.info(f"Symptom Analysis Query: {symptoms}")

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )

    prompt = f"""
Analyze symptoms and return JSON ONLY.

Symptoms: "{symptoms}"

JSON Format:
{{
  "potential_causes": ["..."],
  "severity": "mild|moderate|severe",
  "recommended_actions": ["...", "..."],
  "warning_signs": ["...", "..."]
}}
"""

    try:
        response = llm.invoke(prompt)
        logger.info("Symptom analysis completed.")
        return response.content
    except Exception as e:
        log_exception("Gemini Symptom Analysis Failed", e)
        return None


def generate_final_report(user_query):
    logger.info(f"Final report generation for: {user_query}")

    if any(w in user_query.lower() for w in ["pain", "fever", "cough", "i have"]):
        route = "both"
    else:
        route = "knowledge"

    result = {"route": route}

    if route in ["symptoms", "both"]:
        result["symptom_analysis"] = symptom_analysis(user_query)

    if route in ["knowledge", "both"]:
        summary, docs = rag_query(user_query)
        result["rag_summary"] = summary
        result["evidence"] = [d.page_content[:500] for d in docs] if docs else []

    logger.info("Final report ready.")
    return result


###############################################################
# UI
###############################################################
st.title("🩺 Smart Doctor Assistant")

st.sidebar.header("📄 Upload PDFs")
pdf = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())
    with st.spinner("Indexing PDF..."):
        chunks = embed_pdf("temp.pdf")
    if chunks > 0:
        st.sidebar.success(f"Indexed {chunks} chunks.")
    else:
        st.sidebar.error("PDF failed.")

st.subheader("💬 Ask a Medical Question")
query = st.text_input("Enter your symptoms or medical question...")

if st.button("Analyze"):
    if not query.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Analyzing..."):
            result = generate_final_report(query)

        st.success("Ready!")
        st.write("### 🧠 Route:", result["route"])

        if "symptom_analysis" in result:
            st.write("### 🩺 Symptom Analysis")
            st.code(result["symptom_analysis"], language="json")

        if "rag_summary" in result:
            st.write("### 📚 RAG Summary")
            st.write(result["rag_summary"])

        if "evidence" in result:
            st.write("### 🔍 Evidence (Unique)")
            for idx, ev in enumerate(result["evidence"]):
                st.markdown(f"**Evidence {idx+1}:**")
                st.write(ev)
                st.divider()


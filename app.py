# app.py
import os
os.environ["STREAMLIT_TELEMETRY_DISABLED"] = "1"
os.environ["OTEL_SDK_DISABLED"] = "true"

import streamlit as st

st.set_page_config(
    page_title="Smart Doctor's Assistant",
    page_icon="👨‍⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from uuid import uuid4
from core.config import Settings
from core.logger import get_logger
from core.vector_db import load_vector_db
from services.embedder import embed_pdf
from services.final_report import generate_report
from ui.components import render_sidebar, render_main_area, render_result_card
from ui.styles import get_custom_css

# Inject custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)



# ---------------------------
# INIT
# ---------------------------
settings = Settings()
logger = get_logger()
vector_db = load_vector_db(settings)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "latest_result" not in st.session_state:
    st.session_state.latest_result = None

# ---------------------------
# SIDEBAR + SETTINGS + HISTORY
# ---------------------------
ui_settings = render_sidebar(settings)


# ---------------------------
# MAIN UI LAYOUT
# ---------------------------
left, right = st.columns([1, 1], gap="large")


# LEFT PANEL: Query + Upload + Index
with left:
    query, index_pdf_clicked, uploaded_file = render_main_area()

    # PDF Index
    if index_pdf_clicked and uploaded_file:
        tmp = "uploaded.pdf"
        with open(tmp, "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("🔄 Indexing PDF... Please wait"):
            count = embed_pdf(tmp, vector_db, settings)

        if count > 0:
            st.success(f"✅ Successfully indexed {count} chunks from the document!")
        else:
            st.error("❌ Failed to index PDF. Please check the file format and try again.")
    elif index_pdf_clicked and not uploaded_file:
        st.warning("⚠️ Please upload a PDF file first before indexing.")

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    analyze_clicked = st.button(
        "🔍 Analyze Symptoms", 
        use_container_width=True, 
        type="primary",
        help="Click to analyze your symptoms and get medical insights"
    )



# RIGHT PANEL: Results container
with right:
    result_container = st.container()
    if st.session_state.latest_result:
        render_result_card(result_container, st.session_state.latest_result)


# ---------------------------
# ANALYZE BUTTON HANDLER
# ---------------------------
if analyze_clicked:
    if not query.strip():
        st.error("⚠️ Please enter your symptoms or medical question before analyzing.")
    else:
        with st.spinner("🔬 Analyzing your symptoms... This may take a moment"):
            output = generate_report(
                query=query,
                vector_store=vector_db,
                settings=settings,
                temperature=ui_settings["temperature"],
                top_k=ui_settings["top_k"],
            )

        # VALIDATION FIX: If model returns empty → display fallback text
        if not output or (
             not output.get("rag_summary") and 
             not output.get("symptom_analysis")
        ):
            output = {
                "route": "knowledge",
                "rag_summary": "⚠️ Unable to generate a meaningful response. Please try rephrasing your question with more specific details.",
            }

        entry = {
            "id": str(uuid4()),
            "query": query,
            "result": output,
        }

        st.session_state.chat_history.append(entry)
        st.session_state.latest_result = entry
        render_result_card(result_container, entry)


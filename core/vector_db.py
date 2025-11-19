import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def load_vector_db(settings):
    settings.validate()

    embeddings = GoogleGenerativeAIEmbeddings(
        model=settings.EMBED_MODEL,
        google_api_key=settings.GOOGLE_API_KEY
    )

    return Chroma(
        persist_directory=settings.DB_DIR,
        embedding_function=embeddings
    )

from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.logger import get_logger
import os

logger = get_logger()

def embed_pdf(path, vector_db, settings):
    if not os.path.exists(path):
        logger.error(f"File not found: {path}")
        return 0

    try:
        logger.info(f"Loading PDF from {path}")
        loader = PDFPlumberLoader(path)
        docs = loader.load()
        
        if not docs:
            logger.warning("No pages loaded from PDF")
            return 0
            
        # Check if any text was extracted
        total_text_len = sum(len(d.page_content) for d in docs)
        if total_text_len == 0:
            logger.warning("PDF loaded but no text extracted (scanned PDF?)")
            return 0
            
        logger.info(f"Loaded {len(docs)} pages. Total text length: {total_text_len}")

    except Exception as e:
        logger.error(f"Failed to load PDF: {str(e)}")
        return 0

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(docs)
    logger.info(f"Split into {len(chunks)} chunks")

    if not chunks:
        return 0

    try:
        vector_db.add_documents(chunks)
        # persist() is often auto-handled but we keep it if the method exists
        if hasattr(vector_db, 'persist'):
            vector_db.persist()
        logger.info(f"Successfully added {len(chunks)} chunks to Vector DB")
        return len(chunks)
    except Exception as e:
        logger.error(f"Failed to add documents to Vector DB: {str(e)}")
        return 0

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def embed_pdf(path, vector_db, settings):
    try:
        loader = PyPDFLoader(path)
        docs = loader.load()
    except:
        return 0

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(docs)

    try:
        vector_db.add_documents(chunks)
        vector_db.persist()
        return len(chunks)
    except:
        return 0

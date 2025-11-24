from langchain_google_genai import ChatGoogleGenerativeAI

from core.logger import get_logger

logger = get_logger()

def run_rag(query, vector_db, settings, top_k, temperature):
    evidence_parts = []
    
    # Get documents from vector database
    try:
        logger.info(f"Retrieving documents for query: {query} with top_k={top_k}")
        retriever = vector_db.as_retriever(search_kwargs={"k": top_k})
        docs = retriever.invoke(query)
        logger.info(f"Retrieved {len(docs)} documents")
        
        seen = set()
        unique = []
        for d in docs:
            if d.page_content not in seen:
                seen.add(d.page_content)
                unique.append(d)
        
        logger.info(f"Found {len(unique)} unique documents")
        
        if unique:
            db_evidence = "\n\n---\n\n".join([d.page_content for d in unique])
            evidence_parts.append(f"**From Medical Knowledge Base:**\n{db_evidence}")
            logger.info("Added evidence from knowledge base")
        else:
            logger.warning("No unique documents found after filtering")

    except Exception as e:
        logger.warning(f"Vector DB retrieval failed: {str(e)}")
        unique = []
    
    if not evidence_parts:
        logger.info("No evidence found in RAG, returning empty.")
        return None, unique
    
    evidence = "\n\n==========\n\n".join(evidence_parts)

    llm = ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=temperature,
        max_output_tokens=2048,
    )

    prompt = f"""You are a medical knowledge assistant. Based on the following medical information from the knowledge base, provide a comprehensive and detailed response to the user's query.

User Query: {query}

Medical Information:
{evidence}

Instructions:
1. Synthesize information from the knowledge base
2. Provide a detailed, well-structured response
3. Include relevant medical information
4. Explain concepts clearly and thoroughly
5. Use bullet points or numbered lists when appropriate
6. If the information covers multiple aspects, organize them into sections
7. Be comprehensive but clear

Provide your detailed response:"""

    try:
        response = llm.invoke(prompt)
        return response.content, unique
    except Exception as e:
        logger.error(f"LLM invocation failed: {str(e)}")
        return None, unique

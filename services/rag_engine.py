from langchain_google_genai import ChatGoogleGenerativeAI
from services.google_search import search_google
from core.logger import get_logger

logger = get_logger()

def run_rag(query, vector_db, settings, top_k, temperature):
    evidence_parts = []
    
    # Get documents from vector database
    try:
        retriever = vector_db.as_retriever(search_kwargs={"k": top_k})
        docs = retriever.invoke(query)
        
        seen = set()
        unique = []
        for d in docs:
            if d.page_content not in seen:
                seen.add(d.page_content)
                unique.append(d)
        
        if unique:
            db_evidence = "\n\n---\n\n".join([d.page_content for d in unique])
            evidence_parts.append(f"**From Medical Knowledge Base:**\n{db_evidence}")
    except Exception as e:
        logger.warning(f"Vector DB retrieval failed: {str(e)}")
        unique = []
    
    # Get Google Search results
    try:
        google_results = search_google(query, num_results=3)
        if google_results:
            google_evidence = "\n\n".join([
                f"Source: {r['url']}\n{r['content']}" 
                for r in google_results
            ])
            evidence_parts.append(f"**From Web Search:**\n{google_evidence}")
    except Exception as e:
        logger.warning(f"Google search failed: {str(e)}")
    
    if not evidence_parts:
        return None, unique
    
    evidence = "\n\n==========\n\n".join(evidence_parts)

    llm = ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=temperature,
        max_output_tokens=2048,
    )

    prompt = f"""You are a medical knowledge assistant. Based on the following medical information from multiple sources, provide a comprehensive and detailed response to the user's query.

User Query: {query}

Medical Information:
{evidence}

Instructions:
1. Synthesize information from both the knowledge base and web sources
2. Provide a detailed, well-structured response
3. Include relevant medical information from all sources
4. Explain concepts clearly and thoroughly
5. Use bullet points or numbered lists when appropriate
6. If the information covers multiple aspects, organize them into sections
7. Be comprehensive but clear
8. Cite sources when mentioning specific information

Provide your detailed response:"""

    try:
        response = llm.invoke(prompt)
        return response.content, unique
    except Exception as e:
        logger.error(f"LLM invocation failed: {str(e)}")
        return None, unique

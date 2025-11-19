from langchain_google_genai import ChatGoogleGenerativeAI

def run_rag(query, vector_db, settings, top_k, temperature):
    try:
        retriever = vector_db.as_retriever(search_kwargs={"k": top_k})
        docs = retriever.invoke(query)
    except:
        return None, None

    # Deduplicate
    seen = set()
    unique = []
    for d in docs:
        if d.page_content not in seen:
            seen.add(d.page_content)
            unique.append(d)

    evidence = "\n\n---\n\n".join([d.page_content for d in unique])

    llm = ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=temperature,
    )

    prompt = f"""
Summarize clearly:
{evidence}
"""
    try:
        response = llm.invoke(prompt)
        return response.content, unique
    except:
        return None, unique

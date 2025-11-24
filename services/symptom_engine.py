from langchain_google_genai import ChatGoogleGenerativeAI
from core.logger import get_logger

logger = get_logger()

def analyze_symptoms(symptoms: str, settings, temperature: float, context: str = ""):
    llm = ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=temperature,
        max_output_tokens=2048,
    )

    context_section = ""
    if context:
        context_section = f"""
Context from Patient's Uploaded Medical Report:
{context}

Note: The user has uploaded a medical report. If their query asks about specific details (like "is fever mentioned in the report?"), use the context above to answer. If the context doesn't contain the information, explicitly state that it's not found in the uploaded segments.
"""

    prompt = f"""You are an experienced medical assistant providing detailed symptom analysis.

Patient's Query/Symptoms:
{symptoms}
{context_section}

Please provide a comprehensive analysis including:

1. **Possible Conditions**: What these symptoms might indicate (list 2-3 possibilities)
2. **Severity Assessment**: How serious these symptoms could be
3. **Recommended Actions**: What the person should do next (immediate steps)
4. **Warning Signs**: Critical symptoms that require immediate medical attention
5. **Self-Care Tips**: Things they can do at home to manage symptoms
6. **When to Seek Help**: Specific situations when they should see a doctor

Instructions:
- If the user asks about their specific report, prioritize the 'Context' provided above.
- If the query is general, provide general medical advice based on the symptoms.
- Provide a detailed, well-organized response with clear sections. Be thorough but easy to understand."""

    try:
        resp = llm.invoke(prompt)
        return resp.content
    except Exception:
        logger.exception("Symptom analysis failed")
        return "Unable to analyze symptoms right now."

from langchain_google_genai import ChatGoogleGenerativeAI
from core.logger import get_logger

logger = get_logger()

def analyze_symptoms(symptoms: str, settings, temperature: float):
    llm = ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=temperature,
        max_output_tokens=2048,
    )

    prompt = f"""You are an experienced medical assistant providing detailed symptom analysis.

Patient's Symptoms:
{symptoms}

Please provide a comprehensive analysis including:

1. **Possible Conditions**: What these symptoms might indicate (list 2-3 possibilities)
2. **Severity Assessment**: How serious these symptoms could be
3. **Recommended Actions**: What the person should do next (immediate steps)
4. **Warning Signs**: Critical symptoms that require immediate medical attention
5. **Self-Care Tips**: Things they can do at home to manage symptoms
6. **When to Seek Help**: Specific situations when they should see a doctor

Provide a detailed, well-organized response with clear sections. Be thorough but easy to understand."""

    try:
        resp = llm.invoke(prompt)
        return resp.content
    except Exception:
        logger.exception("Symptom analysis failed")
        return "Unable to analyze symptoms right now."

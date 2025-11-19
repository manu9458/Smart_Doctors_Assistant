# services/symptom_engine.py
from langchain_google_genai import ChatGoogleGenerativeAI
from core.logger import get_logger

logger = get_logger()

def analyze_symptoms(symptoms: str, settings, temperature: float):
    """
    Return a plain-language symptom interpretation (no JSON).
    """
    llm = ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=temperature,
    )

    prompt = f"""
You are a medical assistant.

Analyze these symptoms and return a clear explanation in human language.

Symptoms:
"{symptoms}"

Your answer should include:
- What these symptoms might indicate
- How severe it could be
- What the person should do next
- Warning signs to watch for

DO NOT return JSON. Write a clean medical explanation.
"""

    try:
        resp = llm.invoke(prompt)
        return resp.content
    except Exception:
        logger.exception("Symptom analysis failed")
        return "Unable to analyze symptoms right now."

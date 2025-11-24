# services/final_report.py
from core.logger import get_logger
from services.rag_engine import run_rag
from services.symptom_engine import analyze_symptoms

logger = get_logger()

def generate_report(query: str, vector_store, settings, temperature: float, top_k: int):
    """
    Decide route (symptom vs knowledge vs both), run symptom analysis and RAG as needed,
    and return a dict with results.
    """
    low = query.lower()
    triggers = ["pain", "fever", "cough", "i have", "headache", "nausea"]
    use_symptom = any(t in low for t in triggers)

    route = "both" if use_symptom else "knowledge"
    report = {"route": route}

    # Run RAG first to get context for both routes
    summary, docs = run_rag(query, vector_store, settings, top_k=top_k, temperature=temperature)
    report["rag_summary"] = summary
    report["evidence"] = [d.page_content[:500] for d in docs] if docs else []

    # Prepare context for symptom analysis
    context_text = ""
    if docs:
        context_text = "\n\n".join([d.page_content for d in docs])

    if use_symptom:
        report["symptom_analysis"] = analyze_symptoms(query, settings, temperature, context=context_text)

    logger.info("Report generated.")
    return report

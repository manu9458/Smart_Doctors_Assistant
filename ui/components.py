import streamlit as st
from ui.styles import get_icons

icons = get_icons()

# ------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------
def render_sidebar(settings):
    st.sidebar.markdown(f"## {icons['settings']} Settings")
    
    st.sidebar.markdown("### Model Parameters")
    temp = st.sidebar.slider(
        "🌡️ Temperature", 
        0.0, 1.0, 
        float(settings.DEFAULT_TEMP),
        help="Controls randomness in responses. Lower = more focused, Higher = more creative"
    )
    top_k = st.sidebar.slider(
        "📊 Top-K Retriever", 
        1, 20, 
        int(settings.DEFAULT_TOP_K),
        help="Number of relevant documents to retrieve"
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {icons['history']} Recent History")

    history = st.session_state.get("chat_history", [])

    if not history:
        st.sidebar.info("No queries yet. Start by asking a question!")
    else:
        st.sidebar.markdown(f"*Showing last {min(len(history), 10)} queries*")
        for idx, rec in enumerate(reversed(history[-10:])):
            label = rec["query"][:35] + "..." if len(rec["query"]) > 35 else rec["query"]
            if st.sidebar.button(
                f"{icons['search']} {label}", 
                key=f"history_{rec['id']}",
                use_container_width=True
            ):
                st.session_state.latest_result = rec
                st.rerun()

    st.sidebar.markdown("---")
    if st.sidebar.button(
        "🗑️ Clear All History", 
        use_container_width=True,
        type="secondary"
    ):
        st.session_state.chat_history = []
        st.session_state.latest_result = None
        st.rerun()

    # Add info section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.info(
        f"{icons['doctor']} **Smart Doctor's Assistant**\n\n"
        "AI-powered medical analysis using Google Gemini and RAG technology."
    )

    return {"temperature": temp, "top_k": top_k}


# ------------------------------------------------------
# MAIN AREA
# ------------------------------------------------------
def render_main_area():
    # Header with icon
    st.markdown(
        f"<h1>{icons['doctor']} Smart Doctor's Assistant</h1>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        "<p style='font-size: 1.1rem; color: #64748b; margin-bottom: 2rem;'>"
        "Describe your symptoms or ask medical questions. Our AI will analyze and provide insights.</p>",
        unsafe_allow_html=True
    )

    # Feature badges
    st.markdown(
        f"<div style='margin-bottom: 1.5rem;'>"
        f"<span class='feature-badge'>{icons['symptoms']} Symptom Analysis</span>"
        f"<span class='feature-badge'>{icons['knowledge']} Medical Knowledge</span>"
        f"<span class='feature-badge'>{icons['report']} RAG-Powered</span>"
        f"</div>",
        unsafe_allow_html=True
    )

    # Query input
    query = st.text_area(
        "💬 Describe your symptoms or question:",
        height=150,
        placeholder="Example: I have been experiencing persistent headaches and dizziness for the past 3 days...",
        help="Be as detailed as possible for better analysis"
    )

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    
    # PDF upload section
    st.markdown(f"### {icons['upload']} Upload Medical Documents (Optional)")
    st.markdown(
        "<p style='color: #64748b; font-size: 0.9rem; margin-bottom: 1rem;'>"
        "Upload PDF medical reports to enhance the knowledge base</p>",
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        uploaded = st.file_uploader(
            "Choose a PDF file",
            type=["pdf"],
            help="Upload medical reports, research papers, or clinical documents"
        )
    with col2:
        index_pdf = st.button(
            "📥 Index PDF", 
            use_container_width=True,
            type="secondary"
        )

    return query, index_pdf, uploaded


# ------------------------------------------------------
# RESULT CARD (PROFESSIONAL DESIGN)
# ------------------------------------------------------
def render_result_card(container, record):
    container.empty()
    if not record:
        return

    query = record.get("query", "")
    result = record.get("result", {})

    # Prevent empty boxes
    if not result.get("symptom_analysis") and not result.get("rag_summary"):
        with container:
            st.markdown(
                "<div class='result-card'>"
                f"<div class='query-display'>{icons['search']} <strong>Query:</strong> {query}</div>"
                f"<div style='text-align: center; padding: 2rem;'>"
                f"<p style='font-size: 1.1rem; color: #64748b;'>{icons['info']} No results found. Please try rephrasing your question or provide more details.</p>"
                "</div>"
                "</div>",
                unsafe_allow_html=True
            )
        return

    with container:
        # Get route type for badge
        route = result.get('route', 'N/A')
        badge_class = {
            'knowledge': 'badge-knowledge',
            'symptoms': 'badge-symptoms',
            'both': 'badge-both'
        }.get(route, 'badge-knowledge')
        
        route_icon = {
            'knowledge': icons['knowledge'],
            'symptoms': icons['symptoms'],
            'both': icons['both']
        }.get(route, icons['info'])

        # Result card header
        st.markdown(
            "<div class='result-card'>"
            "<div class='result-header'>"
            f"<div class='result-icon'>{icons['report']}</div>"
            "<div style='flex: 1;'>"
            "<h2 class='result-title'>Analysis Results</h2>"
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

        # Query display
        st.markdown(
            f"<div class='query-display'>"
            f"{icons['search']} <strong>Your Query:</strong> {query}"
            "</div>",
            unsafe_allow_html=True
        )

        # Route badge
        st.markdown(
            f"<span class='badge {badge_class}'>{route_icon} {route.upper()}</span>",
            unsafe_allow_html=True
        )

        # Symptom Analysis Section
        if result.get("symptom_analysis"):
            st.markdown(
                "<div class='result-section'>"
                f"<h3>{icons['symptoms']} Symptom Analysis</h3>"
                f"<p>{result['symptom_analysis']}</p>"
                "</div>",
                unsafe_allow_html=True
            )

        # Medical Knowledge Section
        if result.get("rag_summary"):
            st.markdown(
                "<div class='result-section'>"
                f"<h3>{icons['knowledge']} Medical Knowledge Summary</h3>"
                f"<p>{result['rag_summary']}</p>"
                "</div>",
                unsafe_allow_html=True
            )

        # Disclaimer
        st.markdown(
            "<div class='disclaimer'>"
            f"<strong>{icons['warning']} Medical Disclaimer:</strong> This analysis is for informational purposes only "
            "and should not replace professional medical advice. Always consult with a qualified healthcare provider "
            "for proper diagnosis and treatment."
            "</div>",
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)


# ------------------------------------------------------
# LOADING ANIMATION
# ------------------------------------------------------
def show_loading_message(message="Analyzing your query..."):
    """Display a professional loading message"""
    st.markdown(
        f"<div style='text-align: center; padding: 2rem;'>"
        f"<p style='font-size: 1.1rem; color: #0066cc;'>{icons['analysis']} {message}</p>"
        "</div>",
        unsafe_allow_html=True
    )

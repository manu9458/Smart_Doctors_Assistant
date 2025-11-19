import streamlit as st

# ------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------
def render_sidebar(settings):
    st.sidebar.title("⚙️ Settings")

    temp = st.sidebar.slider("Temperature", 0.0, 1.0, float(settings.DEFAULT_TEMP))
    top_k = st.sidebar.slider("Top-K Retriever", 1, 20, int(settings.DEFAULT_TOP_K))

    st.sidebar.write("---")
    st.sidebar.header("📜 History")

    history = st.session_state.get("chat_history", [])

    if not history:
        st.sidebar.write("No history yet.")
    else:
        for rec in reversed(history[-10:]):
            label = rec["query"][:40] + "..." if len(rec["query"]) > 40 else rec["query"]
            if st.sidebar.button(label, key=f"history_{rec['id']}"):
                st.session_state.latest_result = rec
                st.experimental_rerun()

    st.sidebar.write("---")
    if st.sidebar.button("Clear History"):
        st.session_state.chat_history = []
        st.session_state.latest_result = None
        st.experimental_rerun()

    return {"temperature": temp, "top_k": top_k}


# ------------------------------------------------------
# MAIN AREA
# ------------------------------------------------------
def render_main_area():
    st.header("🩺 Smart Doctor Assistant")

    query = st.text_area(
        "Describe your symptoms or question:",
        height=150,
        placeholder="e.g., I have fever and body pain..."
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        uploaded = st.file_uploader("Upload medical report (PDF)", type=["pdf"], label_visibility="collapsed")
    with col2:
        index_pdf = st.button("Index PDF", use_container_width=True)

    return query, index_pdf, uploaded


# ------------------------------------------------------
# RESULT CARD (WITH FIXED HEIGHT + INTERNAL SCROLL)
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
            st.markdown(f"### Query: {query}")
            st.info("No result found. Try rephrasing your question.")
        return

    with container:
        st.markdown(f"### Query: {query}")

        st.markdown("<div class='result-scroll-box-fixed'>", unsafe_allow_html=True)

        st.write(f"**Type:** {result.get('route', 'N/A')}")

        if result.get("symptom_analysis"):
            st.subheader("Symptom Interpretation")
            st.write(result["symptom_analysis"])

        if result.get("rag_summary"):
            st.subheader("Medical Summary")
            st.write(result["rag_summary"])

        st.markdown("</div>", unsafe_allow_html=True)

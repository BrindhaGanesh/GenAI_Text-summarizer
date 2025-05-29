import streamlit as st
from transformers import pipeline

# App title
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")
st.title("📝 AI Text Summarizer")
st.write("Enter any long text and get a concise summary using a generative AI model.")

# Load model once per session
if "summarizer" not in st.session_state:
    with st.spinner("Loading the model... (only on first run)"):
        st.session_state.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# User input
input_text = st.text_area("✏️ Paste your text here:", height=300)

# Summary length sliders
col1, col2 = st.columns(2)
with col1:
    min_len = st.slider("Minimum summary length", 10, 100, 30)
with col2:
    max_len = st.slider("Maximum summary length", 30, 300, 100)

# Generate summary if button is clicked and input is not empty
if st.button("🔍 Summarize", key="summarize_btn"):
    if input_text.strip():
        with st.spinner("Generating summary..."):
            try:
                summary = st.session_state.summarizer(
                    input_text,
                    max_length=max_len,
                    min_length=min_len,
                    do_sample=False
                )[0]['summary_text']

                st.subheader("📌 Summary")
                st.success(summary)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter some text to summarize.")

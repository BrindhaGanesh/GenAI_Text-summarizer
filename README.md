# 📝 AI Text Summarizer

This is a simple **Generative AI** application that summarizes long text into concise summaries using a **pretrained transformer model**. Built with **Streamlit** and **Hugging Face Transformers**, this app provides an interactive web interface for customizing the length of the summary.

---

## 🚀 Features

- Abstractive summarization using `facebook/bart-large-cnn`
- Summary length customization (min/max tokens)

---

## 🧠 Model

- **Model name**: [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)
- **Pipeline used**:
  ```python
  pipeline("summarization", model="facebook/bart-large-cnn")
---
## ▶️ Running the App
Start the  app using:
```python
streamlit run text_summarizer_app.py

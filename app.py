import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import torch.nn.functional as F

# Load model and tokenizer
@st.cache_resource
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained("Krihzak/Telugu-XLM-RoBERTa")
    tokenizer = AutoTokenizer.from_pretrained("Krihzak/Telugu-XLM-RoBERTa", use_fast=False)
    return model, tokenizer

model, tokenizer = load_model()
labels = ["Negative", "Neutral", "Positive"]

# UI
st.title("Telugu Sentiment Analysis with XLM-RoBERTa")
st.markdown("Enter Telugu text below and click **Predict** to see the sentiment.")

text = st.text_area("Telugu Text Input", height=150)

if st.button("Predict"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)
            pred_class = torch.argmax(probs, dim=1).item()
            confidence = probs[0][pred_class].item()
        
        st.success(f"**Sentiment:** {labels[pred_class]} ({confidence*100:.2f}%)")

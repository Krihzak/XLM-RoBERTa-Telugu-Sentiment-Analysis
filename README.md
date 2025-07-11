Telugu Sentiment Analysis using XLM-RoBERTa

This project provides a fine-tuned **XLM-RoBERTa** model specifically for **Telugu sentiment analysis**.  
It is built on a custom-labeled dataset derived from the **CC100 Telugu corpus**.

---

## 🧠 Overview

- **Model:** [XLM-RoBERTa](https://huggingface.co/facebook/xlm-roberta-base)
- **Task:** Sentiment Classification (e.g., Positive, Negative, Neutral)
- **Language:** Telugu 🇮🇳
- **Dataset:** Custom dataset created from the raw **CC100-Telugu** dump  
- **Frameworks:** 🤗 Transformers, PyTorch, Streamlit

---

## 📂 Dataset Creation

1. Downloaded the **CC100 Telugu** dataset.
2. Cleaned and preprocessed the raw text (removed noise, non-Telugu, and duplicate content).
3. Used the **XLM-RoBERTa model** to weakly label the dataset using zero-shot or semi-supervised methods.
4. Balanced and structured the dataset for sentiment classification.
5. Fine-tuned the base model on the labeled dataset.

---

## ❗ Model Files

> Model files will be uploaded to Hugging Face later  
https://huggingface.co/Krihzak/Telugu-XLM-RoBERTa

---

## 🛠 Installation

```bash
git clone https://github.com/Krihzak/XLM-RoBERTa-Telugu-Sentiment-Analysis.git
cd XLM-RoBERTa-Telugu-Sentiment-Analysis
pip install -r requirements.txt
streamlit run app.py
```

🔍 Demo
Try the model in real time using our Streamlit web app (hosted on Streamlit Cloud).


🧾 Example Predictions

Input (Telugu)	Predicted Sentiment

ఇది చాలా మంచి సినిమా	Positive
కథ నన్ను ఆకట్టుకోలేదు	Negative
సాధారణ చిత్రమే	Neutral

📌 TODO
 Host model on Hugging Face

 Improve labeling quality

 Add confusion matrix in Streamlit

 Extend to other languages



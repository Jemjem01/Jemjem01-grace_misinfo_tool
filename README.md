# 🧠 Grace – AI-Powered Misinformation Detector

Grace is an intelligent tool designed to detect, analyze, and explain misinformation in real time. Built for journalists, educators, and everyday users, it combines natural language processing, explainability, and credibility scoring to help people critically evaluate digital content.

---

## 🚀 Live Demo
👉 [Try the app on Streamlit](https://jemjem01-gracemisinfotool-by6fnweaquwp9pehdptuaz.streamlit.app/)

---

## 💡 Features

| Category         | Capabilities                                                                 |
|------------------|-------------------------------------------------------------------------------|
| **Detection**     | Classifies claims as “Likely True” or “Likely False” using NLP              |
| **Explainability**| Highlights sensational language and provides reasoning                      |
| **Credibility Scoring**| Scores input based on known sources and linguistic cues              |
| **User Interface**| Simple Streamlit app with real-time feedback                                |

---

## 🏗️ Architecture Overview

- **Frontend**: Streamlit
- **Backend**: Python
- **Model**: DistilBERT (via HuggingFace Transformers)
- **Explainability**: Keyword-based mock SHAP/LIME
- **Credibility Engine**: Source-weighted scoring via `sources.json`

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Jemjem01/Jemjem01-grace_misinfo_tool.git
cd Jemjem01-grace_misinfo_tool

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

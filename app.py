import streamlit as st
from misinfo_model import analyze_claim
from explain import get_explanation
from utils import score_credibility

st.set_page_config(page_title="Grace – Misinformation Detector", layout="centered")

st.title("🧠 Grace: AI-Powered Misinformation Detection")
user_input = st.text_area("Paste a headline, tweet, or claim:")

if st.button("Analyze"):
    if user_input:
        label, confidence = analyze_claim(user_input)
        score = score_credibility(user_input)
        explanation = get_explanation(user_input)

        st.markdown(f"### 🧾 Result: **{label}** ({confidence*100:.1f}%)")
        st.progress(confidence)
        st.markdown(f"### 📊 Credibility Score: **{score}/100**")
        st.markdown("### 🔍 Explanation:")
        st.write(explanation)
    else:
        st.warning("Please enter some text to analyze.")

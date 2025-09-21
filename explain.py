def get_explanation(text):
    # Placeholder for SHAP/LIME logic
    keywords = ["shocking", "never seen", "breaking", "exclusive"]
    flagged = [word for word in keywords if word in text.lower()]
    if flagged:
        return f"Flagged sensational language: {', '.join(flagged)}"
    return "No sensational markers detected."

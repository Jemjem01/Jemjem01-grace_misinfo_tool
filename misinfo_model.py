from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased")

def analyze_claim(text):
    result = classifier(text)[0]
    label = "Likely True" if result['label'] == 'LABEL_1' else "Likely False"
    confidence = result['score']
    return label, confidence

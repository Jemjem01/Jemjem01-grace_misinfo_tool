import json

def score_credibility(text):
    with open("sources.json") as f:
        sources = json.load(f)
    score = 50  # base score
    for keyword, weight in sources.items():
        if keyword.lower() in text.lower():
            score += weight
    return min(score, 100)

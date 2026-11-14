import re
from typing import Dict, Any

POSITIVE_WORDS = {
    "happy", "grateful", "calm", "joy", "peace", "excited", "good", "great",
    "awesome", "love", "hope", "accomplished", "proud", "better", "energized"
}

NEGATIVE_WORDS = {
    "sad", "anxious", "depressed", "angry", "tired", "exhausted", "stressed",
    "lonely", "overwhelmed", "terrible", "bad", "awful", "scared", "worried"
}

def analyze_sentiment(text: str) -> Dict[str, Any]:
    """Fast, transparent lexicon-based sentiment polarity analyzer (-1.0 to 1.0)."""
    words = re.findall(r"\b[a-z]+\b", text.lower())
    if not words:
        return {"polarity": 0.0, "subjectivity": 0.5, "dominant_emotion": "Neutral"}

    pos_count = sum(1 for w in words if w in POSITIVE_WORDS)
    neg_count = sum(1 for w in words if w in NEGATIVE_WORDS)
    total_sentiment_words = pos_count + neg_count

    if total_sentiment_words == 0:
        polarity = 0.0
    else:
        polarity = round((pos_count - neg_count) / max(1, total_sentiment_words), 3)

    subjectivity = round(min(1.0, total_sentiment_words / max(5, len(words) * 0.3)), 2)

    if polarity > 0.25:
        emotion = "Positive & Hopeful"
    elif polarity < -0.25:
        emotion = "Vulnerable / Stressed"
    else:
        emotion = "Calm & Reflective"

    return {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "dominant_emotion": emotion,
        "positive_word_count": pos_count,
        "negative_word_count": neg_count
    }

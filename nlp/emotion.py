def detect_emotion(text):
    """
    Simple rule-based emotion detector.
    Returns one of: Stress, Frustration, Confusion, Joy, Neutral
    """
    text_lower = text.lower()

    if any(word in text_lower for word in ["stressed", "pressure", "overwhelmed"]):
        return "Stress"
    if any(word in text_lower for word in ["frustrated", "annoyed", "angry"]):
        return "Frustration"
    if any(word in text_lower for word in ["confused", "unsure", "don't know", "lost"]):
        return "Confusion"
    if any(word in text_lower for word in ["happy", "glad", "excited", "thank", "thanks"]):
        return "Joy"

    return "Neutral"

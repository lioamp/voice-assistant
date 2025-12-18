def detect_emotion(text):
    """
    Enhanced rule-based emotion detector.
    Returns one of: Stress, Frustration, Confusion, Joy, Neutral
    """
    text_lower = text.lower()

    # Stress / anxiety / pressure
    stress_keywords = [
        "stressed", "overwhelmed", "anxious", "pressure", "panic", "nervous",
        "deadline", "burdened", "tense", "strained", "overloaded"
    ]
    if any(word in text_lower for word in stress_keywords):
        return "Stress"

    # Frustration / anger / upset
    frustration_keywords = [
        "frustrated", "angry", "upset", "annoyed", "mad", "irritated",
        "disappointed", "furious", "resentful", "bothered", "agitated"
    ]
    if any(word in text_lower for word in frustration_keywords):
        return "Frustration"

    # Confusion / uncertainty
    confusion_keywords = [
        "confused", "lost", "uncertain", "don’t understand", "unsure",
        "puzzled", "perplexed", "bewildered", "unclear", "uncertainty", "muddled"
    ]
    if any(word in text_lower for word in confusion_keywords):
        return "Confusion"

    # Joy / happiness / excitement
    joy_keywords = [
        "happy", "excited", "thrilled", "pleased", "grateful", "relieved",
        "satisfied", "glad", "delighted", "joyful", "cheerful", "elated",
        "content", "ecstatic"
    ]
    if any(word in text_lower for word in joy_keywords):
        return "Joy"

    # Fallback
    return "Neutral"
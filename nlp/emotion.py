def detect_emotion(text):
    """
    Enhanced rule-based emotion detector.
    Returns one of:
    Stress, Frustration, Confusion, Joy, Gratitude, Anxiety, Excitement,
    Relief, Contentment, Sadness, Surprise, Neutral
    """
    text_lower = text.lower()

    # Gratitude
    gratitude_keywords = ["thank", "thanks", "appreciate", "grateful", "thankful"]
    if any(word in text_lower for word in gratitude_keywords):
        return "Gratitude"

    # Joy / happiness / positive
    joy_keywords = ["happy", "thrilled", "pleased", "glad", "delighted", "joyful",
                    "cheerful", "elated", "ecstatic", "smiling", "laughing"]
    if any(word in text_lower for word in joy_keywords):
        return "Joy"

    # Stress / anxiety / pressure
    stress_keywords = ["stressed", "overwhelmed", "anxious", "pressure", "panic",
                       "nervous", "deadline", "burdened", "tense", "strained",
                       "overloaded", "pressured", "burned out"]
    if any(word in text_lower for word in stress_keywords):
        return "Anxiety"

    # Frustration / anger / upset
    frustration_keywords = ["frustrated", "angry", "upset", "annoyed", "mad",
                            "irritated", "disappointed", "furious", "resentful",
                            "bothered", "agitated", "distraught"]
    if any(word in text_lower for word in frustration_keywords):
        return "Frustration"

    # Confusion / uncertainty
    confusion_keywords = ["confused", "lost", "uncertain", "don’t understand",
                          "unsure", "puzzled", "perplexed", "bewildered",
                          "unclear", "uncertainty", "muddled"]
    if any(word in text_lower for word in confusion_keywords):
        return "Confusion"

    # Sadness / disappointment
    sadness_keywords = ["sad", "unhappy", "depressed", "heartbroken", "miserable"]
    if any(word in text_lower for word in sadness_keywords):
        return "Sadness"

    # Surprise / amazement
    surprise_keywords = ["surprised", "amazed", "astonished", "shocked", "startled"]
    if any(word in text_lower for word in surprise_keywords):
        return "Surprise"

    # Relief / contentment
    relief_keywords = ["relieved", "satisfied", "content", "calm", "peaceful"]
    if any(word in text_lower for word in relief_keywords):
        return "Relief"

    # Excitement / motivation
    excitement_keywords = ["motivated", "energized", "enthusiastic", "pumped"]
    if any(word in text_lower for word in excitement_keywords):
        return "Excitement"

    # Fallback
    return "Neutral"

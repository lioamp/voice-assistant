def classify_intent(text):
    """
    Enhanced rule-based intent classifier.
    Returns one of: Advice_Request, Vent, Information, Gratitude, Neutral
    """
    text_lower = text.lower()

    # Gratitude / positive acknowledgement
    gratitude_keywords = [
        "thank", "thanks", "appreciate", "grateful", "thankful", "pleased",
        "happy with", "glad", "gratitude", "obliged", "thank you", "appreciated",
        "kudos", "well done", "good job", "awesome", "excellent"
    ]
    if any(word in text_lower for word in gratitude_keywords):
        return "Gratitude"

    # Advice / guidance request
    advice_keywords = [
        "help", "advice", "what should i", "how do i", "guidance",
        "recommend", "suggest", "should i", "tips", "assist", "direction", "what to do",
        "best way", "procedure", "strategy", "plan", "solution", "approach"
    ]
    if any(word in text_lower for word in advice_keywords):
        return "Advice_Request"

    # Vent / expressing frustration, worry, or negative emotion
    vent_keywords = [
        "stressed", "worried", "frustrated", "angry", "confused", "upset",
        "overwhelmed", "panic", "tired", "annoyed", "disappointed", "mad",
        "furious", "resentful", "bothered", "distraught", "anxious", "overloaded",
        "tense", "burned out", "pressured", "worst", "problem", "issue"
    ]
    if any(word in text_lower for word in vent_keywords):
        return "Vent"

    # Information sharing / requesting updates
    info_keywords = [
        "update", "report", "news", "progress", "information", "status",
        "data", "results", "current", "latest", "overview", "figures", "numbers",
        "metrics", "summary", "timeline", "schedule", "agenda"
    ]
    if any(word in text_lower for word in info_keywords):
        return "Information"

    # Default fallback
    return "Neutral"

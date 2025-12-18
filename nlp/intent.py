def classify_intent(text):
    """
    Simple rule-based intent classifier.
    Returns one of: Advice_Request, Vent, Information, Gratitude, Neutral
    """
    text_lower = text.lower()
    
    # Gratitude keywords
    if any(word in text_lower for word in ["thank", "thanks", "appreciate", "grateful"]):
        return "Gratitude"
    
    # Advice keywords
    if any(word in text_lower for word in ["help", "advice", "what should i", "how do i", "guidance"]):
        return "Advice_Request"
    
    # Vent / frustration
    if any(word in text_lower for word in ["stressed", "worried", "frustrated", "angry", "confused"]):
        return "Vent"
    
    # Information sharing
    if any(word in text_lower for word in ["update", "report", "news", "progress", "information"]):
        return "Information"
    
    return "Neutral"

from audio.speech_to_text import transcribe_audio
from nlp.sentiment import analyze_sentiment
from nlp.intent import classify_intent
from nlp.emotion import detect_emotion

# Map similar or redundant actions to canonical forms
ACTION_MAP = {
    # Positive reinforcement
    "Acknowledge and reinforce positive behavior": "Reinforce positive behavior",
    "Reinforce positive behavior and encourage continuation": "Reinforce positive behavior",
    "Reinforce positive outcomes and encourage continuation": "Reinforce positive behavior",
    "Reinforce current approach": "Reinforce positive behavior",
    "Reinforce positive outcomes": "Reinforce positive behavior",
    
    # Empathy / stress relief / support
    "Offer empathy or stress-relief suggestions": "Provide empathy and support",
    "Offer empathy and problem-solving steps": "Provide empathy and support",
    "Provide empathy and problem solving": "Provide empathy and support",
    "Suggest stress-relief techniques or prioritize tasks": "Provide stress-relief suggestions",
    "Provide stress-relief suggestions": "Provide stress-relief suggestions",
    "Provide empathy and support": "Provide empathy and support",
    
    # Guidance / actionable instructions
    "Provide actionable guidance or recommendations": "Provide actionable guidance",
    "Clarify instructions and objectives": "Provide actionable guidance",
    "Provide clear instructions or clarify objectives": "Provide actionable guidance",
    "Acknowledge and clarify unexpected developments": "Provide actionable guidance",
    "Encourage and channel energy positively": "Provide actionable guidance",
    
    # Information / updates
    "Provide clear and concise updates": "Provide clear and concise updates"
}

def process_audio(audio_file):
    """
    Core processing function for the voice assistant.
    Returns transcription, sentiment, intent, emotion, insight, and canonical suggested actions.
    """
    text = transcribe_audio(audio_file)
    sentiment, scores = analyze_sentiment(text)
    intent = classify_intent(text)
    emotion = detect_emotion(text)

    actions = []

    # Sentiment-based actions
    if sentiment == "positive":
        insight = "User expresses positive engagement or satisfaction."
        actions.append("Reinforce current approach")
        if intent in ["Gratitude", "Advice_Request"]:
            actions.append("Acknowledge and reinforce positive behavior")
    elif sentiment == "negative":
        insight = "User expresses dissatisfaction, concern, or pressure."
        actions.extend([
            "Identify the main source of concern",
            "Clarify constraints or deadlines",
            "Break the issue into manageable steps"
        ])
    else:
        insight = "User expresses neutral or unclear sentiment."
        actions.extend([
            "Gather more context",
            "Clarify the user's objective"
        ])

    # Intent-based actions
    if intent == "Advice_Request":
        actions.append("Provide actionable guidance or recommendations")
    elif intent == "Vent":
        actions.append("Offer empathy or stress-relief suggestions")
    elif intent == "Information":
        actions.append("Provide clear and concise updates")
    elif intent == "Gratitude":
        actions.append("Reinforce positive behavior and encourage continuation")

    # Emotion-based actions
    emotion_action_map = {
        "Stress": "Provide stress-relief suggestions",
        "Anxiety": "Provide stress-relief suggestions",
        "Frustration": "Provide empathy and problem solving",
        "Confusion": "Clarify instructions and objectives",
        "Joy": "Reinforce positive behavior",
        "Gratitude": "Reinforce positive behavior",
        "Sadness": "Provide empathy and support",
        "Surprise": "Acknowledge and clarify unexpected developments",
        "Relief": "Reinforce positive outcomes",
        "Excitement": "Encourage and channel energy positively"
    }

    if emotion in emotion_action_map:
        actions.append(emotion_action_map[emotion])

    # Deduplicate and canonicalize
    deduped_actions = []
    for action in actions:
        canonical = ACTION_MAP.get(action, action)
        if canonical not in deduped_actions:
            deduped_actions.append(canonical)

    return {
        "text": text,
        "sentiment": sentiment,
        "scores": scores,
        "intent": intent,
        "emotion": emotion,
        "insight": insight,
        "actions": deduped_actions
    }

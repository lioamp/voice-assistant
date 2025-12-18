from audio.speech_to_text import transcribe_audio
from nlp.sentiment import analyze_sentiment
from nlp.intent import classify_intent
from nlp.emotion import detect_emotion

# Map similar actions to canonical forms
ACTION_MAP = {
    "Acknowledge and reinforce positive behavior": "Reinforce positive behavior",
    "Reinforce positive behavior and encourage continuation": "Reinforce positive behavior",
    "Reinforce positive outcomes and encourage continuation": "Reinforce positive behavior",
    "Offer empathy or stress-relief suggestions": "Provide empathy and stress relief",
    "Offer empathy and problem-solving steps": "Provide empathy and problem solving",
    "Provide actionable guidance or recommendations": "Provide actionable guidance",
    "Suggest stress-relief techniques or prioritize tasks": "Provide stress-relief suggestions",
    "Provide clear instructions or clarify objectives": "Clarify instructions and objectives"
}

def process_audio(audio_file):
    """
    Core processing function for the voice assistant.
    Returns a dictionary with transcription, sentiment, intent, emotion,
    insight, and deduplicated, canonical suggested actions.
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
        if intent == "Gratitude":
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
    if emotion == "Stress":
        actions.append("Suggest stress-relief techniques or prioritize tasks")
    elif emotion == "Frustration":
        actions.append("Offer empathy and problem-solving steps")
    elif emotion == "Confusion":
        actions.append("Provide clear instructions or clarify objectives")
    elif emotion == "Joy":
        actions.append("Reinforce positive outcomes and encourage continuation")

    # Deduplicate and map to canonical forms
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

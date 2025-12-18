# engine.py
from audio.speech_to_text import transcribe_audio
from nlp.sentiment import analyze_sentiment
from nlp.intent import classify_intent
from nlp.emotion import detect_emotion

def process_audio(audio_file):
    """
    Core processing function for the voice assistant.
    Takes an audio file, returns transcription, sentiment, intent, emotion,
    insight, and suggested actions.
    """
    # Transcribe speech
    text = transcribe_audio(audio_file)

    # Analyze sentiment
    sentiment, scores = analyze_sentiment(text)

    # Classify intent
    intent = classify_intent(text)

    # Detect emotion
    emotion = detect_emotion(text)

    # Generate insight and suggested actions based on sentiment
    if sentiment == "positive":
        insight = "User expresses positive engagement or satisfaction."
        actions = ["Reinforce current approach", "Explore opportunities to build on momentum"]
    elif sentiment == "negative":
        insight = "User expresses dissatisfaction, concern, or pressure."
        actions = ["Identify the main source of concern", "Clarify constraints or deadlines", "Break the issue into manageable steps"]
    else:
        insight = "User expresses neutral or unclear sentiment."
        actions = ["Gather more context", "Clarify the user's objective"]

    # Tailor actions based on intent
    if intent == "Advice_Request":
        actions.append("Provide actionable advice or guidance")
    elif intent == "Vent":
        actions.append("Offer empathy or stress-relief suggestions")
    elif intent == "Gratitude":
        actions.append("Acknowledge and reinforce positive behavior")

    # Tailor actions based on emotion
    if emotion == "Stress":
        actions.append("Suggest stress-relief techniques or prioritize tasks")
    elif emotion == "Frustration":
        actions.append("Offer empathy and problem-solving steps")
    elif emotion == "Confusion":
        actions.append("Provide clear instructions or clarify objectives")
    elif emotion == "Joy":
        actions.append("Reinforce positive behavior and encourage continuation")

    return text, sentiment, scores, intent, emotion, insight, actions

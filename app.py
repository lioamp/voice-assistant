import time
from audio.mic_input import record_audio
from audio.speech_to_text import transcribe_audio
from nlp.sentiment import analyze_sentiment
from nlp.intent import classify_intent
from nlp.emotion import detect_emotion
from output.formatter import format_output

MIC_INDEX = 1  # replace with your mic's index from sd.query_devices()
DURATION = 5   # seconds to record

def main():
    print(f"Recording will start in 3 seconds. Please get ready to speak...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    audio_file = record_audio(filename="input.wav", duration=DURATION, device=MIC_INDEX)
    
    text = transcribe_audio(audio_file)

    sentiment, scores = analyze_sentiment(text)

    intent = classify_intent(text)

    emotion = detect_emotion(text)

    # Insight logic
    # Actions based on sentiment
    if sentiment == "negative":
        insight = "User expresses dissatisfaction, concern, or pressure."
        actions = [
            "Identify the main source of concern",
            "Clarify constraints or deadlines",
            "Break the issue into manageable steps"
        ]
    elif sentiment == "positive":
        insight = "User expresses positive engagement or satisfaction."
        actions = [
            "Reinforce current approach",
            "Explore opportunities to build on momentum"
        ]
    else:
        insight = "User expresses neutral or unclear sentiment."
        actions = [
            "Gather more context",
            "Clarify the user's objective"
        ]

    # Actions based on intent
    if intent == "Advice_Request":
        actions.append("Provide actionable advice or guidance")
    elif intent == "Vent":
        actions.append("Offer empathy or stress-relief suggestions")
    elif intent == "Gratitude":
        actions.append("Acknowledge and reinforce positive behavior")

    # Actions based on emotion
    if emotion == "Stress":
        actions.append("Suggest stress-relief techniques or prioritize tasks")
    elif emotion == "Frustration":
        actions.append("Offer empathy and problem-solving steps")
    elif emotion == "Confusion":
        actions.append("Provide clear instructions or clarify objectives")
    elif emotion == "Joy":
        actions.append("Reinforce positive behavior and encourage continuation")


    # Include intent in the output
    format_output(text, sentiment, scores, insight, actions, intent=intent, emotion=emotion)

if __name__ == "__main__":
    main()

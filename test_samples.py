from nlp.sentiment import analyze_sentiment
from nlp.intent import classify_intent
from nlp.emotion import detect_emotion
from decision.engine import ACTION_MAP
from output.formatter import format_output

def deduplicate_actions(actions):
    """Deduplicate and canonicalize actions."""
    deduped = []
    for action in actions:
        canonical = ACTION_MAP.get(action, action)
        if canonical not in deduped:
            deduped.append(canonical)
    return deduped[:5]  # limit to 5 actions for readability

def process_audio_text_only(text):
    """Process a text string for testing purposes."""
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

    deduped_actions = deduplicate_actions(actions)

    return {
        "text": text,
        "sentiment": sentiment,
        "scores": scores,
        "intent": intent,
        "emotion": emotion,
        "insight": insight,
        "actions": deduped_actions
    }

# -------------------------
# Sample sentences to test
# -------------------------
test_sentences = [
    "I'm extremely stressed about finishing this report on time.",
    "Thank you so much for your guidance, it really helped me!",
    "Can you give me advice on how to handle this client issue?",
    "I feel frustrated because nothing seems to work as expected.",
    "I'm happy we managed to complete the project ahead of schedule!",
    "I don't understand what steps I should take next.",
    "Here is the latest update on our progress with the tasks.",
    "I feel overwhelmed and anxious about all these deadlines."
]

# Run tests
if __name__ == "__main__":
    for idx, sentence in enumerate(test_sentences, 1):
        print(f"\n--- Test {idx} ---")
        result = process_audio_text_only(sentence)
        format_output(result)

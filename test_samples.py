from nlp.sentiment import analyze_sentiment
from nlp.intent import classify_intent
from nlp.emotion import detect_emotion
from decision.engine import ACTION_MAP
from output.formatter import format_output

def deduplicate_actions(actions):
    """Deduplicate and canonicalize actions, limit to 5 for readability."""
    deduped = []
    for action in actions:
        canonical = ACTION_MAP.get(action, action)
        if canonical not in deduped:
            deduped.append(canonical)
    return deduped[:5]

def process_audio_text_only(text):
    """Process a text string for testing purposes with full enhanced intent and emotion mapping."""
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
    intent_action_map = {
        "Advice_Request": "Provide actionable guidance or recommendations",
        "Vent": "Provide empathy and support",
        "Information": "Provide clear and concise updates",
        "Gratitude": "Reinforce positive behavior and encourage continuation"
    }
    if intent in intent_action_map:
        actions.append(intent_action_map[intent])

    # Emotion-based actions (expanded)
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

    # Deduplicate actions and limit for readability
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
    "I feel overwhelmed and anxious about all these deadlines.",
    "I'm excited about the upcoming team event!",
    "I am relieved the project was completed successfully.",
    "I feel sad about missing the deadline yesterday.",
    "Wow, I'm surprised by the unexpected changes in the schedule."
]

# Run tests
if __name__ == "__main__":
    for idx, sentence in enumerate(test_sentences, 1):
        print(f"\n--- Test {idx} ---")
        result = process_audio_text_only(sentence)
        format_output(result)

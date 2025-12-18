def format_output(text, sentiment, scores, insight, actions, intent=None, emotion=None):
    print("\n=== TRANSCRIPTION ===")
    print(text)

    print("\n=== ANALYSIS ===")
    print(f"Sentiment: {sentiment}")
    print(f"Scores: {scores}")

    if intent:
        print(f"Intent: {intent}")
    if emotion:
        print(f"Emotion: {emotion}")

    print("\n=== INSIGHT ===")
    print(insight)

    print("\n=== SUGGESTED ACTIONS ===")
    for i, action in enumerate(actions, 1):
        print(f"{i}. {action}")

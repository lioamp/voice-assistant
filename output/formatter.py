def format_output(result):
    """
    Nicely formats and prints the assistant's results.
    Expects a dictionary from process_audio().
    """
    print("\n=== TRANSCRIPTION ===")
    print(result["text"])

    print("\n=== ANALYSIS ===")
    print(f"Sentiment: {result['sentiment']}")
    print(f"Scores: {result['scores']}")
    print(f"Intent: {result['intent']}")
    print(f"Emotion: {result['emotion']}")

    print("\n=== INSIGHT ===")
    print(result["insight"])

    print("\n=== SUGGESTED ACTIONS ===")
    for idx, action in enumerate(result["actions"], 1):
        print(f"{idx}. {action}")

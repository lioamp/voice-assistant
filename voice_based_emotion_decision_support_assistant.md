# 🎙️ Voice-Based Emotion & Decision Support Assistant

## Overview
This project is a **voice-driven analytical decision support system** that converts spoken input into **structured, text-based insights**.

The system analyzes speech to detect **sentiment, emotion, and user intent**, then outputs **explainable insights and suggested courses of action** in text form. It does **not** function as a conversational voice assistant; instead, it behaves like an **analytics engine** that uses voice as its input modality.

Rather than treating sentiment analysis as an end goal, this system uses it as an **input to decision-making**, aligning with principles from **natural language processing (NLP)** and **decision support systems (DSS)**.

The project is designed as a **portfolio-grade system** that demonstrates system design, NLP fundamentals, and human-centered analytics.

---

## Key Features
- 🎤 Speech-to-text input via microphone
- 🙂 Sentiment analysis (positive / neutral / negative)
- 🧠 Emotion detection (e.g., stress, frustration, confusion)
- 🎯 Intent classification (e.g., venting, decision support, help-seeking)
- 🧩 Rule-based decision engine for action recommendations
- 🗣️ Optional text-to-speech responses
- 🔍 Explainable and transparent logic

---

## System Architecture

```
Microphone Input
      ↓
Speech-to-Text (ASR)
      ↓
Text Analysis Layer
   ├─ Sentiment Analysis
   ├─ Emotion Recognition
   ├─ Intent Classification
   └─ Context Tracking
      ↓
Decision Engine (Rule-Based)
      ↓
Suggested Course of Action
```

### Design Rationale
- **Modular architecture** allows each component to be improved independently
- **Rule-based decisions** ensure explainability and user trust
- Separation of analysis and decision logic follows established DSS principles

---

## Technologies Used

- **Python** – Core implementation language
- **Speech-to-Text** – OpenAI Whisper (or equivalent ASR)
- **NLP Libraries** – NLTK / scikit-learn
- **Sentiment Analysis** – Lexicon-based baseline (VADER)
- **Intent Classification** – TF-IDF + Logistic Regression
- **Text-to-Speech (Optional)** – pyttsx3 or cloud TTS

---

## Methodology

### 1. Speech-to-Text
Audio is captured through a microphone and converted into text using an Automatic Speech Recognition (ASR) model. This enables downstream text-based analysis.

### 2. Text Processing
The transcribed text undergoes preprocessing:
- Lowercasing
- Tokenization
- Stopword removal

### 3. Sentiment & Emotion Analysis
- Sentiment polarity is detected using a lexicon-based approach
- Emotional states (e.g., stress, frustration) are inferred using a multi-class classifier

### 4. Intent Classification
User intent is identified through supervised text classification. Common intent categories include:
- `venting`
- `ask_for_help`
- `decision_support`
- `information_request`

### 5. Decision Engine
A rule-based inference engine maps emotion and intent to recommended actions.

Example rule:
```
IF emotion = stress AND intent = decision_support
THEN suggest breaking the task into smaller steps
```

This approach prioritizes **interpretability over black-box automation**.

---

## Example Interaction

**User (spoken input):**
> "I’m really stressed about my deadline and I don’t know what to do."

**System Output (text-based):**
```text
TRANSCRIPTION:
I’m really stressed about my deadline and I don’t know what to do.

ANALYSIS:
- Sentiment: Negative
- Emotion: Stress
- Intent: Decision Support

INSIGHT:
User expresses time pressure and uncertainty related to task completion.

SUGGESTED ACTIONS:
1. Break the deadline into smaller, manageable tasks
2. Identify the most urgent deliverable
3. Allocate focused time blocks for completion
```

---

## Evaluation Approach

- Sentiment and intent models are evaluated using standard classification metrics
- System behavior is assessed qualitatively based on the relevance and appropriateness of recommendations

---

## Limitations
- Sarcasm and highly implicit emotion remain challenging
- Emotion detection relies primarily on textual cues rather than vocal tone
- Rule-based logic may not generalize to all scenarios

These limitations are acknowledged as areas for future improvement.

---

## Ethical Considerations
- No long-term storage of raw voice recordings
- Transparent decision logic
- Recommendations are **advisory**, not prescriptive
- System is not intended to replace human judgment

---

## Future Improvements
- Incorporate vocal prosody features (tone, pitch, pace)
- Add contextual memory across longer conversations
- Explore adaptive or hybrid rule–ML decision logic
- Deploy as a web or desktop application

---

## Why This Project Matters
This project demonstrates how sentiment analysis can be transformed from a passive analytical output into an **active decision-support input**. It showcases practical applications of NLP, explainable AI, and system design in a human-centered context.

---

## Author
**Carlos Virgilio C. Amparo**  
Business Analytics & IT


import time
from audio.mic_input import record_audio
from output.formatter import format_output
from decision.engine import process_audio

MIC_INDEX = 1  # replace with your mic's index from sd.query_devices()
DURATION = 5   # seconds to record

def main():
    print("Recording will start in 3 seconds. Please get ready to speak...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    audio_file = record_audio(filename="input.wav", duration=DURATION, device=MIC_INDEX)

    text, sentiment, scores, intent, emotion, insight, actions = process_audio(audio_file)

    format_output(text, sentiment, scores, insight, actions, intent=intent, emotion=emotion)

if __name__ == "__main__":
    main()

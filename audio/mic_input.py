import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="input.wav", duration=5, sample_rate=44100, device=None):
    """
    Records audio from the microphone and saves it to a WAV file.
    
    Args:
        filename (str): Name of the output WAV file.
        duration (int): Duration of recording in seconds.
        sample_rate (int): Sampling rate.
        device (int or None): Microphone device index (None = default mic).
    """
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        device=device
    )
    sd.wait()
    write(filename, sample_rate, audio)
    print(f"Recording saved to {filename}")
    return filename

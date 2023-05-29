import openai
import sounddevice as sd
import soundfile as sf


def get_voice_input():
    """
    Gets voice input from user
    - record voice input until user stops recording
    - save audio file
    - return audio file path
    """
    duration = 5.0  # seconds
    samplerate = 48000  # Hz
    microphone_id = 1  # Use sd.query_devices() to select your recording device in channels
    print('Recording...')
    myrecording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=microphone_id, blocking=True)
    print('Recording stopped')
    filename = 'voice_input.wav'
    sf.write(filename, myrecording, samplerate)
    audio_file = open(filename, "rb")
    return audio_file


def speech_to_text():
    """
    Converts speech to text
    https://platform.openai.com/docs/guides/speech-to-text
    """
    audio_file = get_voice_input()
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"] #sends string

from elevenlabs import generate, play


def text_to_speech(response):
    print("Sending to TTS")
    audio = generate(
        text=response,
        voice="Domi",
        model="eleven_multilingual_v1",
    )
    play(audio)

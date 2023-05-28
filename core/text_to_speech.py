from elevenlabs import generate, play


def text_to_speech(response):
    audio = generate(
        text=response,
        voice="Domi",
        model="eleven_multilingual_v1",
    )
    play(audio)

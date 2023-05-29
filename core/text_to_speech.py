from elevenlabs import generate, play


def text_to_speech(response):
    print("Sending to TTS")
    print (response)
    audio = generate(
        text=response,
        voice="Domi",
        model="eleven_multilingual_v1",
    )
    play(audio)

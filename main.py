from core.chat_gpt import process_question, get_chat_gpt_response
from core.config import configure_openai
from core.config import configure_voice_bot
from core.speech_to_text import speech_to_text
from core.text_to_speech import text_to_speech


def record_and_give_response():
    configure_voice_bot()
    configure_openai()
    question = speech_to_text()
    response = get_chat_gpt_response(question) # sending: string
    text_to_speech(response)


def main():
    record_and_give_response()


if __name__ == '__main__':
    main()

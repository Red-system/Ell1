import os

import openai
from dotenv import load_dotenv
from elevenlabs import set_api_key

load_dotenv()


def configure_openai():
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.organization = os.getenv('OPENAI_ORG')


def configure_voice_bot():
    set_api_key(os.getenv('ELEVENLABS_API_KEY'))

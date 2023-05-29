import numpy
import openai
import webbrowser


def process_question(question):
    #question is string
    to_chatGPT = ["passe", "mode", "créatif"]
    to_process = question.split()
    #to_process is a list

    if all(item in to_process for item in to_chatGPT):
       return get_chat_gpt_response(question)
    else:
        return get_google_response(question)


def get_google_response(question):
    webbrowser.open('https://www.google.com/search?=q=' + question)


def get_chat_gpt_response(question):
    """
    take a sentence in and return a CHATGPT response
    :param text:
    :return:
    """
    print("sending: " + question + " to Chat GPT")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content
    print("Chat GPT said: " + result)
    return result


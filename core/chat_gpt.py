import openai


def get_chat_gpt_response(question):
    """
    take a sentence in and return a CHATGPT response
    :param text:
    :return:
    """
    print("sending: "+question+" to Chat GPT")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content
    print("Chat GPT said: "+result)
    return result

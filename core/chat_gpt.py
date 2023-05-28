import openai


def get_chat_gpt_response(question):
    """
    take a sentence in and return a CHATGPT response
    :param text:
    :return:
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    return result

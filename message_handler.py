


def extract_message(request_as_json):
    message = request_as_json["message"]
    return message


def extract_message_chat_id(message):
    chat_id = message['message']['chat']['id']
    return chat_id


def extract_message_user_name(message):
    user_name = message['from']['id']
    return user_name


def extract_message_text(message):
    text = message['text']
    return text


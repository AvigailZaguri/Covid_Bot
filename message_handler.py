


def extract_message(request_as_json):
    message = request_as_json["message"]
    return message


def extract_message_chat_id(request_as_json):
    chat_id = request_as_json['message']['chat']['id']
    return chat_id


def extract_message_user_name(request_as_json):
    user_name = request_as_json['message']['from']['id']
    return user_name


def extract_message_text(message):
    text = message['text']
    return text


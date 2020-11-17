

import message_handler
import covid_api


def handle_bot(request_as_json):
    message = message_handler.extract_message(request_as_json)
    chat_id = message_handler.extract_message_chat_id(message)
    user_name = message_handler.extract_message_user_name(message)
    return chat_id
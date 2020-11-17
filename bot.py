

import message_handler
import covid_api


def handle_bot(message):
    message_to_split = message['text']
    user_name = message['from']['id']
    # David 20000000 056-88687
    params = message_to_split.split()
    print(params)
    # user_name = message['']
    # message = message_handler.extract_message(request_as_json)
    # chat_id = message_handler.extract_message_chat_id(message)
    # user_name = message_handler.extract_message_user_name(message)
    # text = message_handler.extract_message_user_name(message)
    current_state = covid_api.get_state_by_user_name(user_name)
    print(current_state, " before if")
    if not current_state:
        current_state = 1
        covid_api.set_state_by_user_name(user_name, current_state)
        return covid_api.state_commands[current_state]()
    elif current_state != 2:
        current_state = covid_api.next_state(user_name, current_state)
        print(current_state, " else")
        return covid_api.state_commands[current_state](user_name, params)
    elif current_state == 3:
        return covid_api.state_commands[current_state]()




import message_handler
import covid_api


def handle_bot(request_as_json):
    message_to_split = request_as_json['text']
    user_name = request_as_json['from']['id']
    # David 20000000 056-88687
    params = message_to_split.split()
    current_state = covid_api.get_state_by_user_name(user_name)
    covid_api.state_commands[current_state](params)



    # message = message_handler.extract_message(request_as_json)
    # chat_id = message_handler.extract_message_chat_id(message)
  #   user_name = message_handler.extract_message_user_name(request_as_json)
    # text = message_handler.extract_message_user_name(message)
    # current_state = covid_api.get_state_by_user_name(user_name)
    # if not current_state:
    #     current_state = 1
    #     return covid_api.state_commands[current_state]()
    #
    # else:
    #     current_state = covid_api.next_state(user_name, current_state)
    #     covid_api.state_commands[current_state]()
    # return chat_id


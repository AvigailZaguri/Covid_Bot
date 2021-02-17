import covid_api


def handle_bot(message):
    message_to_split = message['text']
    user_name = message['from']['id']
    params = message_to_split.split()
    current_state = covid_api.get_state_by_user_name(user_name)
    if params[0] == "/start":
        current_state = None
    if not current_state:
        current_state = 1
        covid_api.set_state_by_user_name(user_name, current_state)
        first_name = message['from']['first_name']
        last_name = message['from']['last_name']
        name = first_name + " " + last_name
        return covid_api.state_commands[current_state](user_name, name)
    elif current_state != 300:
        current_state = covid_api.next_state(user_name, current_state)
        return covid_api.state_commands[current_state](user_name, params)
    elif current_state == 300:
        return covid_api.state_commands[current_state](user_name, params)




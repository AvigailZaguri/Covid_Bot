from person import *
from location import *
import dbHandler


def welcome_message():
    return "hello my name is covidbot please enter your name , id , phone"


def identification(user_name, *args):
    name = 'shira'
    user_id = 23456
    phone = 324567
    person = Person(user_name, user_id, name, phone)
    dbHandler.insert_person(person)
    return "The identification process success\n" \
           "Please select command to continue"


def get_state_by_user_name(user_name):
    state = dbHandler.get_state_by_user_name(user_name)
    if not state:
        return None
    return state['Conversation_state']


def set_state_by_user_name(user_name, state):
    dbHandler.set_state_by_user_name(user_name, state)


def next_state(user_name, current_state):
    next_state_num = state_flow[current_state]
    set_state_by_user_name(user_name, next_state_num)
    return next_state_num


def thank_you():
    return "tank you"


state_commands = {1: welcome_message, 2: identification, 3: thank_you}
state_flow = {1: 2, 2: 3}

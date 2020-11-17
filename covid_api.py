
from person import *
from location import *
import dbHandler


def welcome_message():
    return "hello my name is covidbot please enter your name , id , phone"


def identification(self, **kwargs):

    user_name = kwargs["user_name"]
    user_id = kwargs["id"]
    name = kwargs["name"]
    phone = kwargs["phone"]
    state = kwargs["state"]
    person = Person(user_name, user_id, name, phone, state)


def get_state_by_user_name(self, user_name):
    pass


def set_state_by_user_name(self, user_name):
    pass


def next_state(self, user_name, current_state):
    next_state = state_flow[current_state]
    set_state_by_user_name(user_name)
    return next_state


state_commands = {1: welcome_message, 2: identification}
state_flow = {1: 2, 2: 3, 3: 4, 4: 6}
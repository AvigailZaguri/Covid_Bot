from person import *
from location import *
import dbHandler


def welcome_message():
    return "hello my name is covidbot please enter your name , id , phone"


def identification(user_name, args):
    name = args[0]
    user_id = args[1]
    phone = args[2]
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


def which_command(user_name, args):
    if args[0] == "/insulation":
        return flow_insulation(user_name)
    if args[0] == "/epidemiology":
        return flow_epidemiology(user_name)
    if args[0] == "/coronatest":
        return flow_corona_test(user_name)


# 50-100
def flow_insulation(user_name):
    dbHandler.set_state_by_user_name(user_name, 51)
    return "select flow_insulation"


# 101-150
def flow_epidemiology(user_name):
    dbHandler.set_state_by_user_name(user_name, 102)
    return "select flow_epidemiology"


def thank_you(user_name, args):
    return "tank you"


# 151-200
def flow_corona_test(user_name):
    dbHandler.set_state_by_user_name(user_name, 151)
    return "ho, no, so sad you feel sick.\ndo you have fever?"


# 152
def have_fever(user_name, args):
    if args[0] == 'yes':
        return "Are you coughing?"
    elif args[0] == 'no':
        dbHandler.set_state_by_user_name(user_name, 164)
        return "Are you coughing?"
        # return "you probably don't have corona.\nhope you will feel good soon"
    else:
        dbHandler.set_state_by_user_name(user_name, 151)
        return "wrong input, try again\ndo you have fever?"


# 153
def no_fever(user_name, args):
    if args[0] == 'yes':
        return "Do you feel tired?"
        # return "you probably have corona.\ngo check yourself for corona"
    elif args[0] == 'no':
        dbHandler.set_state_by_user_name(user_name, 166)
        return "Do you feel tired?"
        # return "you might have corona.\ngo check yourself for corona"
    else:
        dbHandler.set_state_by_user_name(user_name, 152)
        return "wrong input, try again\nAre you coughing?"


# 154
def have_corona(user_name, args):
    if args[0] == 'yes':
        return "Do you feel tired?"
        # return "you probably have corona.\ngo check yourself for corona"
    elif args[0] == 'no':
        dbHandler.set_state_by_user_name(user_name, 168)
        return "Do you feel tired?"
        # return "you might have corona.\ngo check yourself for corona"
    else:
        dbHandler.set_state_by_user_name(user_name, 153)
        return "wrong input, try again\nAre you coughing?"


# 155
def have_3sym(user_name, args):
    """
        fever, coughing
        :param user_name:
        :param args: yes / no
        :return: message
        """
    if args[0] == 'yes':
        return "You have all the severe symptoms for covid-19\nit's probably because you have covid.\n" \
               "You should take covid-19-test immediately,\nAnd isolate yourself from society"
    elif args[0] == 'no':
        return "Wow, you have fever and you are coughing, and still not tired?!\n" \
               "You should take covid-19-test,\nAnd isolate yourself from society"
    else:
        dbHandler.set_state_by_user_name(user_name, 155)
        return "wrong input, try again\nDo you feel tired?"


# 156
def have_2sym(user_name, args):
    """
        fever, no coughing
        :param user_name:
        :param args: yes / no
        :return: message
        """
    if args[0] == 'yes':
        return "You have two severe symptoms for covid\nYou might have the virus.\n" \
               "but it can be any other virus or bacteria.\n" \
               "Please take a covid-19 test, stay home.\nWe don't want the covid to spread"
    elif args[0] == 'no':
        return "Ho, you just have fever, it's a sign you should go rest\n it's recommended take a covid-19 test, " \
               "stay home.\nWe don't want the covid to spread "
    else:
        dbHandler.set_state_by_user_name(user_name, 166)
        return "wrong input, try again\nDo you feel tired?"


# 157
def have_1sym(user_name, args):
    """
    no fever, do coughing
    :param user_name:
    :param args: yes / no
    :return: message
    """
    if args[0] == 'yes':
        return "You have two severe symptoms for covid\nYou might have the virus.\n" \
               "Please take a covid-19 test, stay home.We don't want the covid to spread"
    elif args[0] == 'no':
        return "You are only coughing, it might be covid-virus\n but I'm not sure...\n" \
               "Maybe it's just a cold, go rest, wish you feel better soon"
    else:
        dbHandler.set_state_by_user_name(user_name, 157)
        return "wrong input, try again\nDo you feel tired?"


# 158
def have_n_sym(user_name, args):
    """
    no fever, no coughing
    :param user_name:
    :param args: yes / no
    :return: message
    """
    if args[0] == 'yes':
        return "You don't have fever, and you are not coughing.\n" \
               "Maybe you didn't sleep so well, and there for you are tired.\n" \
               "Go rest, and I hope you will feel stronger soon"
    elif args[0] == 'no':
        dbHandler.set_state_by_user_name(user_name, 300)
        return "You do not have any severe symptom of Covid.\n" \
               "maybe it's just anxiety to get infected with covid"
    else:
        dbHandler.set_state_by_user_name(user_name, 168)
        return "wrong input, try again\nDo you feel tired?"


def when_daignosed():
    pass


def where_been_day1():
    pass


def where_been_day2():
    pass


def where_been_day3():
    pass


def where_been_day4():
    pass


def finish_epmd():
    pass


state_commands = {1: welcome_message, 2: identification, 3: which_command, 300: thank_you,
                  102: when_daignosed, 103: where_been_day1, 104: where_been_day2, 105: where_been_day3,
                  106: where_been_day4, 107: finish_epmd,
                  152: have_fever, 153: no_fever, 154: have_corona}

state_flow = {1: 2, 2: 3, 3: 300,  # start
              102: 103, 103: 104, 104: 105, 105: 106, 106: 107, 107: 300,  # empd
              151: 152, 152: 153, 153: 155, 154: 157, 155: 300, 156: 300, 157: 300, 158: 300  # coronatest
              }

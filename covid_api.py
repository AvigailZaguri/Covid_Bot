

import personLocation
from person import *
from location import *
import dbHandler
from datetime import date, datetime, timedelta


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
    dbHandler.set_state_by_user_name(user_name, 50)
    return "Where have you been yesterday? please enter the exact: 'place: XXX time: hh:mm'"


# 101-150
def flow_epidemiology(user_name):
    dbHandler.set_state_by_user_name(user_name, 101)
    return "when are you daignosed in Covid19?(yyyy-mm-dd)"


# 151-200
def flow_corona_test(user_name):
    dbHandler.set_state_by_user_name(user_name, 151)
    return "Ho, no, so sad you feel sick.\ndo you have fever?"


def thank_you(user_name, args):
    return "tank you"


def have_fever(user_name, args):
    if args[0] == 'yes':
        return "Are you coughing?"
    elif args[0] == 'no':
        dbHandler.set_state_by_user_name(user_name, 300)
        return "you probably don't have corona.\nhope you will feel good soon"
    else:
        dbHandler.set_state_by_user_name(user_name, 151)
        return "wrong input, try again"


def no_fever(user_name, args):
    if args[0] == 'yes':
        return "you probably have corona.\ngo check yourself for corona"
    elif args[0] == 'no':
        return "you might have corona.\ngo check yourself for corona"
    else:
        dbHandler.set_state_by_user_name(user_name, 152)
        return "wrong input, try again"


def when_daignosed(user_name, args):
    dbHandler.insert_day_daignose(user_name, args[0])
    day_daignosed = datetime.strptime(args[0], '%Y-%m-%d')
    one_day = timedelta(days=1)
    day_before = day_daignosed - one_day
    return f"Where you were on the date {day_before.date()}?\n" \
           f"Please enter: 'address xxxx time hh:mm duration: mm"

#['address','yafo','1','time','10:30','duration','75']
def where_been_day1(user_name, args):
    location = " ".join(args)
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    one_day = timedelta(days=2)
    day_before = day_daignosed - one_day
    #data = geolocator.geocode("1 yaffo , jerusalem, israel")
    #lat, lon = data.raw.get("lat"), data.raw.get("lon")
    # personLocation p_location(234, lat, lon, 1, 2020-10-9, 60, 1)
    # dbHandler.insert_location_person()
    return f"Where you were on the date {day_before.date()}?\n" \
           f"Please enter: 'address xxxx time hh:mm duration: mm"


def where_been_day2(user_name, args):
    pass


def where_been_day3(user_name, args):
    pass


def where_been_day4(user_name, args):
    pass


def finish_epmd(user_name, args):
    pass


def get_yesterday_location_time(user_name, args):
    time_index = args.index("time")
    time = args[time_index + 1]
    print(time)
    place = ""
    for i in range(1, time_index):
        place += args[i] + " "
    place = place.strip()
    print(place)
    # check is red location
    return check_is_red_location(place, time)


def check_is_red_location(location, time):
    if dbHandler.get_location_by_name_and_time(location, time):
        return "It's a red place, please go into isolation"
    else:
        return "It's not a red place, you'r free!"


state_commands = {1: welcome_message, 2: identification, 3: which_command, 300: thank_you,
                  102: when_daignosed, 103: where_been_day1, 104: where_been_day2, 105: where_been_day3,
                  106: where_been_day4, 107: finish_epmd, #bidud
                  152: have_fever, 153: no_fever,
                  51: get_yesterday_location_time, 52: check_is_red_location}
state_flow = {1: 2, 2: 3, 3: 300, #start
              101: 102, 102: 103, 103: 104, 104: 105, 105: 106, 106: 107, 107: 300, #empd
              151: 152, 152: 153, 153: 300, #coronatest
              50: 51,51: 52, 52: 300} #bidud




from personLocation import PersonLocation
from person import *
from location import Location
import dbHandler
from datetime import date, datetime, timedelta
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="bot app")


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
    location_end_index = args.index('time')
    i = 1
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('time') + 1]
    duration = args[args.index('time') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=2)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=1)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, duration, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return f"Where you were on the date {day_before.date()}?\n" \
           f"Please enter: 'address xxxx time hh:mm duration: mm"


def where_been_day2(user_name, args):
    location_end_index = args.index('time')
    i = 1
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('time') + 1]
    duration = args[args.index('time') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=3)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=2)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, duration, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return f"Where you were on the date {day_before.date()}?\n" \
           f"Please enter: 'address xxxx time hh:mm duration: mm"


def where_been_day3(user_name, args):
    location_end_index = args.index('time')
    i = 1
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('time') + 1]
    duration = args[args.index('time') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=4)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=3)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, duration, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return f"Where you were on the date {day_before.date()}?\n" \
           f"Please enter: 'address xxxx time hh:mm duration: mm"


def where_been_day4(user_name, args):
    location_end_index = args.index('time')
    i = 1
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('time') + 1]
    duration = args[args.index('time') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=5)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=4)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, duration, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return f"Tank you for your sincerity in the epidemiological inquiry.\n" \
           f"I wish you to feel good.\n" \
           f"and don't forget-STAY AT HOME ;)"


def finish_epmd(user_name, args):
    return "The epidemiological inquiry ended.\n" \
           "you can start again by the command: /start"


state_commands = {1: welcome_message, 2: identification, 3: which_command, 300: thank_you,
                  102: when_daignosed, 103: where_been_day1, 104: where_been_day2, 105: where_been_day3,
                  106: where_been_day4, 107: finish_epmd,
                  152: have_fever, 153: no_fever}
                 # 50: get_yesterday_location, 51: }
state_flow = {1: 2, 2: 3, 3: 300, #start

              101: 102, 102: 103, 103: 104, 104: 105, 105: 106, 106: 107, 107: 300, #empd

              151: 152, 152: 153, 153: 300 #coronatest
              }

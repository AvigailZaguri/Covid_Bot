from personLocation import PersonLocation

from person import *
from location import Location
import dbHandler
from datetime import date, datetime, timedelta
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="bot app")


# 1
def welcome_message():
    return "Hi, my name is covid-bot\n" \
           "I am here for you!!\n" \
           "what's your name?"


# 4
def insert_name(user_name, args):
    my_name = "".join(args)
    dbHandler.set_name_by_user_name(user_name, my_name)
    return "and what's your id number?"


# 5
def insert_id(user_name, args):
    dbHandler.set_id_by_user_name(user_name, args[0])
    return "and what's your phone number?"


# 2
def identification(user_name, args):
    dbHandler.set_phone_by_user_name(user_name, args[0])
    return "The identification process success\n" \
           "Please select command to continue \n /quarantine \n /epidemiology \n /questioning"


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
    if args[0] == '/start':
        dbHandler.set_state_by_user_name(user_name, 1)
        return "Hi, my name is covid-bot\n" \
               "I'm here for you!!\n" \
               "what's your name?"
    if args[0] == "/quarantine":
        return flow_insulation(user_name)
    if args[0] == "/epidemiology":
        return flow_epidemiology(user_name)
    if args[0] == "/questioning":
        return flow_corona_test(user_name)
    else:
        dbHandler.set_state_by_user_name(user_name, 2)
        return "Wrong command.\n" \
               "please try again."


# 50-100
def flow_insulation(user_name):
    dbHandler.set_state_by_user_name(user_name, 50)
    return "Where have you been yesterday? \n please enter (Yafo 1, Jerusalem at hh:mm, about XXX minutes)"


# 101-150
def flow_epidemiology(user_name):
    dbHandler.set_state_by_user_name(user_name, 101)
    return "when are you daignosed in Covid19?(yyyy-mm-dd)"


# 301
def thank_you():
    return "Thank you:-)\n You prevent covid-19 from spreading!!\n" \
           "Do you want anther command? /yes /no"


# 300
def anther_command(user_name, args):
    if args[0] == '/yes' or args[0] == 'yes':
        dbHandler.set_state_by_user_name(user_name, 2)
        return "Please select command to continue"
    else:
        return "Ready for you anytime\n /start to continue"


# 151-200
def flow_corona_test(user_name):
    dbHandler.set_state_by_user_name(user_name, 151)
    return "Ho, no, so sad you feel sick.\ndo you have fever? /yes /little /no "


# 152
def have_fever(user_name, args):
    if args[0] == '/yes' or args[0] == 'yes':
        return "Are you coughing? /dry_cough /wet_cough /no_cough "
    elif args[0] == '/no' or args[0] == 'no':
        dbHandler.set_state_by_user_name(user_name, 164)
        return "Are you coughing? /dry_cough /wet_cough /no_cough "
    elif args[0] == '/little' or args[0] == 'little':
        dbHandler.set_state_by_user_name(user_name, 164)
        return "Its probably not related to covid\nAre you coughing?  /dry_cough /wet_cough /no_cough "
    else:
        dbHandler.set_state_by_user_name(user_name, 151)
        return "wrong input, try again\ndo you have fever? /yes /little /no"


# 153
def no_fever(user_name, args):
    if args[0] == '/dry_cough' or args[0] == 'dry':
        return "Do you feel tired? /yes /no"
    elif args[0] == '/no_cough' or args[0] == '/wet_cough' or args[0] == 'no' or args[0] == 'wet':
        dbHandler.set_state_by_user_name(user_name, 166)
        return "Do you feel tired? /yes /no"
    else:
        dbHandler.set_state_by_user_name(user_name, 152)
        return "wrong input, try again\nAre you coughing? /dry_cough /wet_cough /no_cough "


# 154
def have_corona(user_name, args):
    if args[0] == '/dry_cough' or args[0] == 'dry':
        return "Do you feel tired? /yes /no"
    elif args[0] == '/no_cough' or args[0] == '/wet_cough' or args[0] == 'no' or args[0] == 'wet':
        dbHandler.set_state_by_user_name(user_name, 168)
        return "Do you feel tired? /yes /no"
    else:
        dbHandler.set_state_by_user_name(user_name, 153)
        return "wrong input, try again\nAre you coughing? /dry_cough /wet_cough /no_cough "


# 155
def have_3sym(user_name, args):
    """
        fever, coughing
        :param user_name:
        :param args: yes / no
        :return: message
        """
    if args[0] == '/yes' or args[0] == 'yes':
        dbHandler.set_state_by_user_name(user_name, 169)
        return "You have all the severe symptoms for covid-19\nit's probably because you have covid.\n" \
               "Do you any other symptoms? /yes /no"
    elif args[0] == '/no' or args[0] == 'no':
        return "Wow, you have fever and you are coughing, and still not tired?!\n" \
               "You should take covid-19-test,\nAnd isolate yourself from society\n\n" + thank_you()
    else:
        dbHandler.set_state_by_user_name(user_name, 155)
        return "wrong input, try again\nDo you feel tired? /yes /no"


# 156
def have_2sym(user_name, args):
    """
        fever, no coughing
        :param user_name:
        :param args: yes / no
        :return: message
        """
    if args[0] == '/yes' or args[0] == 'yes':
        return "You have two severe symptoms for covid\nYou might have the virus.\n" \
               "but it can be any other virus or bacteria.\n" \
               "Please take a covid-19 test, stay home.\nWe don't want the covid to spread\n\n" + thank_you()
    elif args[0] == '/no' or args[0] == 'no':
        return "Ho, you just have fever, it's a sign you should go rest\n it's recommended take a covid-19 test, " \
               "stay home.\nWe don't want the covid to spread \n\n" + thank_you()
    else:
        dbHandler.set_state_by_user_name(user_name, 166)
        return "wrong input, try again\nDo you feel tired? /yes /no"


# 157
def have_1sym(user_name, args):
    """
    no fever, do coughing
    :param user_name:
    :param args: yes / no
    :return: message
    """
    if args[0] == '/yes' or args[0] == 'yes':
        return "You have two severe symptoms for covid\nYou might have the virus.\n" \
               "Please take a covid-19 test, stay home.We don't want the covid to spread\n\n" + thank_you()
    elif args[0] == '/no' or args[0] == 'no':
        return "You are only coughing, it might be covid-virus\n but I'm not sure...\n" \
               "Maybe it's just a cold, go rest, wish you feel better soon\n\n" + thank_you()
    else:
        dbHandler.set_state_by_user_name(user_name, 157)
        return "wrong input, try again\nDo you feel tired? /yes /no"


# 158
def have_n_sym(user_name, args):
    """
    no fever, no coughing
    :param user_name:
    :param args: yes / no
    :return: message
    """
    if args[0] == '/yes' or args[0] == 'yes':
        return "You don't have fever, and you are not coughing.\n" \
               "Maybe you didn't sleep so well, and there for you are tired.\n" \
               "Go rest, and I hope you will feel stronger soon\n\n" + thank_you()
    elif args[0] == '/no' or args[0] == 'no':
        dbHandler.set_state_by_user_name(user_name, 300)
        return "You do not have any severe symptom of Covid.\n" \
               "maybe it's just anxiety to get infected with covid\n\n" + thank_you()
    else:
        dbHandler.set_state_by_user_name(user_name, 168)
        return "wrong input, try again\nDo you feel tired? /yes /no"


# 159
def more_sym(user_name, args):
    """
        fever, coughing, tired
        :param user_name:
        :param args: yes / no
        :return: message
        """
    if args[0] == '/yes' or args[0] == 'yes':
        return "Your condition sounds bad\nit's probably because you have covid.\n" \
               "You should take covid-19-test immediately,\nAnd isolate yourself from society\n\n" + thank_you()
    elif args[0] == '/no' or args[0] == 'no':

        return "I think you should take covid-19-test,\nAnd isolate yourself from society.\n" \
               "Although you don't have other symptoms\n\n" + thank_you()
    else:
        dbHandler.set_state_by_user_name(user_name, 169)
        return "wrong input, try again\nDo you any other symptoms? /yes /no"


# 102
def when_daignosed(user_name, args):
    dbHandler.insert_day_daignose(user_name, args[0])
    day_daignosed = datetime.strptime(args[0], '%Y-%m-%d')
    one_day = timedelta(days=1)
    day_before = day_daignosed - one_day
    return f"Where you were on the date {day_before.date()}?\n" \
           f"Please enter: '<address> at <hh:mm>"


# ['address','yafo','1','time','10:30','duration','75']
# 103
def where_been_day1(user_name, args):
    location_end_index = args.index('at')
    i = 0
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('at') + 1]
    # duration = args[args.index('at') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=2)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=1)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, 0, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return "How much time you spent there?"


# 113
def day1_duration(user_name, args):
    duration = args[0]
    dbHandler.set_duration_by_user_name(user_name, duration)
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=2)
    day_before = day_daignosed - tow_day
    return "Where you in another place that day? /yes /no"


# 114
def day2_duration(user_name, args):
    duration = args[0]
    dbHandler.set_duration_by_user_name(user_name, duration)
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=3)
    day_before = day_daignosed - tow_day
    return "Where you in another place that day? /yes /no"


# 115
def day3_duration(user_name, args):
    duration = args[0]
    dbHandler.set_duration_by_user_name(user_name, duration)
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=4)
    day_before = day_daignosed - tow_day
    return "Where you in another place that day? /yes /no"


# 116
def day4_duration(user_name, args):
    duration = args[0]
    dbHandler.set_duration_by_user_name(user_name, duration)
    return "Where you in another place that day? /yes /no"
    # return f"Tank you for your sincerity in the epidemiological inquiry.\n" \
    #        f"I wish you to feel good.\n" \
    #        f"and don't forget: STAY AT HOME ;)"


# 104
def where_been_day2(user_name, args):
    location_end_index = args.index('at')
    i = 0
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('at') + 1]
    # duration = args[args.index('at') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=3)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=2)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, 0, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return "How much time you spent there?"


def where_been_day3(user_name, args):
    location_end_index = args.index('at')
    i = 0
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('at') + 1]
    # duration = args[args.index('at') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=4)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=3)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, 0, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return "How much time you spent there?"


def where_been_day4(user_name, args):
    location_end_index = args.index('at')
    i = 0
    location = ""
    while i < location_end_index:
        location += " "
        location += args[i]
        i += 1
    hour = args[args.index('at') + 1]
    # duration = args[args.index('at') + 3]
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    tow_day = timedelta(days=5)
    day_before = day_daignosed - tow_day
    data = geolocator.geocode(location).raw
    lat = data.get("lat")
    lon = data.get("lon")
    day_hour = day_daignosed - timedelta(days=4)
    day_hour = day_hour.strftime('%Y-%m-%d') + f" {hour}:00"
    personL = PersonLocation(user_name, lat, lon, 1, day_hour, 0, 1)
    location_obj = Location(lat, lon)
    if not dbHandler.get_location(location_obj):
        dbHandler.insert_location(location_obj)
    dbHandler.insert_location_person(personL)
    return "How much time you spent there?"


# 123

def more_location_day1(user_name, args):
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    if args[0] == "/yes" or args[0] == "yes":
        dbHandler.set_state_by_user_name(user_name, 102)
        one_day = timedelta(days=1)
        day_before = day_daignosed - one_day
        return f"Where you were on the date {day_before.date()}?\n" \
               f"Please enter: '<address> at <hh:mm>"
    elif args[0] == "/no" or args[0] == "no":
        one_day = timedelta(days=2)
        day_before = day_daignosed - one_day
        return f"Where you were on the date {day_before.date()}?\n" \
               f"Please enter: '<address> at <hh:mm>"


# 124
def more_location_day2(user_name, args):
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    if args[0] == "/yes" or args[0] == "yes":
        dbHandler.set_state_by_user_name(user_name, 123)
        one_day = timedelta(days=2)
        day_before = day_daignosed - one_day
        return f"Where you were on the date {day_before.date()}?\n" \
               f"Please enter: '<address> at <hh:mm>"
    elif args[0] == "/no" or args[0] == "no":
        one_day = timedelta(days=3)
        day_before = day_daignosed - one_day
        return f"Where you were on the date {day_before.date()}?\n" \
               f"Please enter: '<address> at <hh:mm>"


# 125
def more_location_day3(user_name, args):
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    if args[0] == "/yes" or args[0] == "yes":
        dbHandler.set_state_by_user_name(user_name, 124)
        one_day = timedelta(days=3)
        day_before = day_daignosed - one_day
        return f"Where you were on the date {day_before.date()}?\n" \
               f"Please enter: '<address> at <hh:mm>"
    elif args[0] == "/no" or args[0] == "no":
        one_day = timedelta(days=4)
        day_before = day_daignosed - one_day
        return f"Where you were on the date {day_before.date()}?\n" \
               f"Please enter: '<address> at <hh:mm>"


# 126
def more_location_day4(user_name, args):
    day_daignosed = dbHandler.get_day_daignose(user_name)[0]['day_daignose']
    day_daignosed = datetime.strptime(day_daignosed, '%Y-%m-%d')
    if args[0] == "/yes" or args[0] == "yes":
        dbHandler.set_state_by_user_name(user_name, 125)
        one_day = timedelta(days=4)
        day_before = day_daignosed - one_day
        return f"Where you were on the date {day_before.date()}?\n" \
               f"Please enter: '<address> at <hh:mm>"
    elif args[0] == "/no" or args[0] == "no":
        one_day = timedelta(days=5)
        day_before = day_daignosed - one_day
        return f"Tank you for your sincerity in the epidemiological inquiry.\n" \
               f"I wish you to feel good.\n" \
               f"and don't forget: STAY AT HOME ;)\n\n" \
               f"do you want another command: /yes /no"


def get_yesterday_location_time(user_name, args):
    print("get_yesterday_location_time")
    print(args)
    time_index = args.index("at")
    duration_index = args.index("about")
    duration = args[duration_index + 1]
    print(duration)
    if int(duration) < 15:
        return "The duration is less than 15 minutes,\n" \
               "you don't have to go into isolation.\n" \
               "if you want to start again click /start"
    time = ""
    time += args[time_index + 1]
    print(time)
    place = ""
    i = 0
    while i < time_index:
        place += " "
        place += args[i]
        i += 1
    # check is red location
    return check_is_red_location(place, time)


def check_is_red_location(place, time):
    print("check is red location")
    print(place)
    print(time)
    data = geolocator.geocode(place).raw
    print(data)
    # need to add here if the address not exist
    lat = data.get("lat")
    lon = data.get("lon")
    time += ':00'
    if dbHandler.is_red_location(lat, lon, time):
        return "It's a red place, please be self quarantine\n" \
               "if you want to start again click /start"
    else:
        return "It's not a red place, you'r free!\n" \
               "if you want to start again click /start"


state_commands = {1: welcome_message, 2: identification, 3: which_command, 300: thank_you,
                  102: when_daignosed, 103: where_been_day1, 104: where_been_day2, 105: where_been_day3,
                  113: day1_duration, 114: day2_duration, 115: day3_duration, 116: day4_duration,
                  106: where_been_day4, 123: more_location_day1, 124: more_location_day2,
                  125: more_location_day3, 126: more_location_day4,
                  152: have_fever, 153: no_fever, 154: have_corona,
                  155: have_3sym, 156: have_2sym, 157: have_1sym, 158: have_n_sym, 159: more_sym,  # corona test
                  300: anther_command,
                  4: insert_name, 5: insert_id, 51: get_yesterday_location_time}  # bidud

# 102-103-113-[123:y(103)/n]-104-114-[124:y(103)/n]-105-115--[125:y(103)/n]106-116--[126:y(103)/n]-107-300

state_flow = {2: 3, 3: 300, 301: 300,  # start
              101: 102, 102: 103, 103: 113, 113: 123, 123: 104, 104: 114, 114: 124, 124: 105, 105: 115, 115: 125,
              125: 106, 106: 116, 116: 126, 126: 300,  # empd
              151: 152, 152: 153, 153: 155, 154: 157, 155: 300, 156: 300, 157: 300, 158: 300, 159: 300,
              164: 154, 166: 156, 168: 158, 169: 159,  # corona test
              50: 51, 51: 300,
              1: 4, 4: 5, 5: 2
              }  # bidud

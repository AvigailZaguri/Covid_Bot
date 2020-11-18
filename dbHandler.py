from config import connection
from person import *
from location import *


def insert_person(person):
    with connection.cursor() as cursor:
        query = f"update person set id = '{person.person_id}'," \
                f"name = '{person.name}'," \
                f"phone = '{person.phone}' " \
                f"where telegramUserName = {person.user_name};"
        cursor.execute(query)
        connection.commit()


def insert_day_daignose(user_name, day_daignose):
    with connection.cursor() as cursor:
        query = f"update person set day_daignose = '{day_daignose}'" \
                f"where telegramUserName = {user_name};"
        cursor.execute(query)
        connection.commit()


def insert_location(location):
    with connection.cursor() as cursor:
        query = f"insert into location values ({location.lat}, {location.lon});"
        cursor.execute(query)
        connection.commit()


def insert_location_person(person_location):
    with connection.cursor() as cursor:
        query = f"insert into LocationPerson values ({person_location.datetime_start}, {person_location.duration}, " \
                f"{person_location.is_mask}" \
                f"{person_location.is_open_space},{person_location.userName},{person_location.lat},{person_location.lon});"
        cursor.execute(query)
        connection.commit()


def is_red_location(lat, lon, date):
    with connection.cursor() as cursor:
        query = f"select * from LocationPerson where lat = {lat} and lon = {lon} and startDateTime.date = {date};"
        cursor.execute(query)
        res = cursor.fetchall()
        if res[0]:
            return True
        return False


def get_date_time_and_duration(lat, lon, date):
    with connection.cursor() as cursor:
        query = f"select * from LocationPerson where lat = {lat} and lon = {lon};"
        cursor.execute(query)
        res = cursor.fetchall()
        return res[0]


def get_state_by_user_name(user_name):
    with connection.cursor() as cursor:
        query = f"select Conversation_state from Person where telegramUserName = {user_name};"
        cursor.execute(query)
        res = cursor.fetchone()
        return res


def set_state_by_user_name(user_name, state):
    if not get_state_by_user_name(user_name):
        with connection.cursor() as cursor:
            query = f"insert into  Person (telegramUserName, Conversation_state) values({user_name}, {state});"
            cursor.execute(query)
            connection.commit()
    else:
        with connection.cursor() as cursor:
            query = f"update  Person set Conversation_state = {state} where telegramUserName = {user_name};"
            cursor.execute(query)
            connection.commit()


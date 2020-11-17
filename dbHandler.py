from config import connection
from person import *
from location import *


def insert_person(person):
    with connection.cursor() as cursor:
        query = f"insert into person values ({person.person_id}, {person.name}, {person.phone}, {person.user_name}, {person.state});"
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


def mok_db():
    with connection.cursor() as cursor:
        query = "insert into person values(209311181, 'aya', 025375858, '0987', 0);"
        cursor.execute(query)
        connection.commit()
        query = "insert into location values('31.75165995', '35.18739009689732');"
        cursor.execute(query)
        connection.commit()
        query = "insert into LocationPerson values('2020-11-16 10:30:00', 75, 1, 0, 0987, '31.75165995', '35.18739009689732');"
        cursor.execute(query)
        connection.commit()


#mok_db()

print(is_red_location('31.75165995', '35.18739009689732', '2020-11-16'))
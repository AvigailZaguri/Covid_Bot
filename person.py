class Person:
    def __init__(self, user_name, person_id, name, phone, day_daignosed=0):
        self.user_name = user_name
        self.person_id = person_id
        self.name = name
        self.phone = phone
        self.day_daignosed = day_daignosed

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_id(self, person_id):
        self.person_id = person_id

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

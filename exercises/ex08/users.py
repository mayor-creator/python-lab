class Users:

    def __init__(self, f_name, l_name, location, country):
        "Initialize attributes to describe a user"
        self.f_name = f_name
        self.l_name = l_name
        self.location = location
        self.country = country

    def greet_user(self):
        return f"Hi, {self.f_name} welcome"

    def describe_user(self):
        return f"{self.f_name} is based in {self.location}, {self.country}"


user_1 = Users("Juliet", "Petit", "Paris", "France")
user_2 = Users("Mayor", "Creator", "Accra", "Ghana")

greetings = user_1.greet_user()
print(greetings)

description = user_2.describe_user()
print(description)

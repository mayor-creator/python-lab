import json


def greet_user():
    filename = "python-lab/lessons/lesson11/json/username.json"

    try:
        with open(filename, "r") as file:
            username = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        username = input("What is your name? ").lower()
        with open(filename, "w") as file:
            json.dump(username, file)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username.title()}!")


greet_user()

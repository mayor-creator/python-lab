import json

filename = "python-lab/lessons/lesson11/json/username.json"

with open(filename, "r") as file:
    username = json.load(file)
    print(f"Welcome back, {username.title()}!")

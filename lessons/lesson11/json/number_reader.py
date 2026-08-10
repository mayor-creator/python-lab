import json

# json.load()

filename = "python-lab/lessons/lesson11/json/numbers.json"

with open(filename, mode="r") as file:
    numbers = json.load(file)

print(numbers)

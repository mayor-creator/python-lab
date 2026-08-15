import json

# dumps() to convert a python dictionary to as JSON-formatted string.
# the dictionary keys will always be strings in JSON.
food_rating = {"organic_dog_food": 2, "human_food": 10}
food_rating_data = json.dumps(food_rating, indent=4)
print(food_rating_data)

# write a json file with dump()
person_data = {
    "name": "juliette",
    "hobbies": ["photography", "reading", "gaming"],
    "address": {"work": "engineer", "home": ["Lyon", "France"]},
    "friends": [
        {"name": "mayor", "hobbies": ["coding", "reading", "running"]},
        {"name": "gloria", "hobbies": ["cooking", "painting"]},
    ],
}

filename = "python-lab/lessons/lesson11/json/examples/person.json"
with open(file=filename, mode="w", encoding="utf-8") as write_file:
    json.dump(person_data, write_file, indent=4)
    print("Data is written to json file.")

# read json file with load()

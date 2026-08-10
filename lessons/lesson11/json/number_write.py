import json

# json.dump() takes two arguments:
# 1. piece of data to store.
# 2. a file object it can use to store the data.
numbers = [2, 3, 5, 7, 11, 13]

filename = "python-lab/lessons/lesson11/json/numbers.json"
with open(filename, "w") as file:
    json.dump(numbers, file)

# list is a collection of ordered items

# creating a list
fruits = ["Apple", "Banana", "Strawberry", "Orange"]

# accessing item in a list
# index of list starts at zero
print(fruits[2])

# changing an item in a list
fruits[0] = "Mango"

# adding an item to the end of a list
fruits.append("Apple")

print(fruits)

# nested list
nested_list = ["A", "B", ["C", "D"]]

# print letter D
letter_d = nested_list[2][1]
print(letter_d)
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

# inserting a new item into a list using position
fruits.insert(2, "Peach")
print(fruits)

# removing an item from a list with del statement
del fruits[0]
print(fruits)

# removing an item from a list with pop method
item_removed = fruits.pop()
print(fruits)
print(f"The last fruit I ate was {item_removed.title()} fruit.")

# popping items from any position in a list
first_fruit = fruits.pop(0)
print(f"The first fruit of the day is {first_fruit} fruit.")

# removing an item by value
bad_fruit = "Strawberry"
fruits.remove(bad_fruit)
print(fruits)

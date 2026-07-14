# Loop allows you to iterate over the items in a collection

# for loop 
# for item in list_of_items:
    # do something to each item

fruits = ["Apple", "Strawberry", "Mango"]
for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")

print(fruits)

student_scores = [180, 124, 165, 173, 189, 169, 146]

max = 0
for high_score in student_scores: 
    if high_score > max:
        max = high_score

print(max)

# range() to generate a range of numbers
# for number in range(a, b, step):
    # do something with the number

for number in range(1, 10, 2): 
    print(number)

print(" ")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)

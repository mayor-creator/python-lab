# if-else statement
# if condition: 
#   do this
# else: 
#   do this

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120: 
    print("You can ride the rollercoaster")
else:
    print("You can't drive")

# comparison operators
# > greater than
# < less than 
# >= greater than or equal to 
# <= less than or equal to 
# == equal to
# (!=) not equal to

# module operator (%) returns the reminder after the division
print("Determine if the number is even or odd")
number = int(input("Enter a number? "))

if number % 2 == 0:
    print(f"{number} is even number")
else: 
    print(f"{number} is odd numbers")

# nested if else statement
# if condition: 
#   if another condition:
#       do this
#   else: 
#       do this
# else: 
#   do this

# if elif else statement
# if condition1:
#   do this
# elif condition2: 
#   do this
# else: 
#   do this

weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)

if bmi < 18.5: 
    print("underweight")
elif bmi < 25: 
    print("normal weight")
else: 
    print("overweight")

print(" ")
print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
cost = 0

if size == "S":
    cost += 15
    if pepperoni == "Y":
        cost += 2
    else: 
        cost += 0
    if extra_cheese == "Y":
        cost += 1
    else:
        cost += 0
elif size == "M":
    cost += 20
    if pepperoni == "Y":
        cost += 3
    else: 
        cost += 0
    if extra_cheese == "Y":
        cost += 1
    else:
        cost += 0
else: 
    cost += 25
    if pepperoni == "Y":
        cost += 3
    else: 
        cost += 0
    if extra_cheese == "Y":
        cost += 1
    else:
        cost += 0

print(f"You final bill is: ${cost}")
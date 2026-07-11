# data types 

# string of characters and created with double quote
# getting the first character of the string with subscripting
print("Hello"[0])

# string
print("123" + "345")

# integers are whole numbers without decimal place
print(20 + 90)

# large integers
print(10_000_00)

# float 
print(3.1419)

# boolean = true or false
print(True)
print(False)

# data types checking
print(type("Lyon"))
print(type(1234))
print(type(3.14))
print(type(True))

# data types conversion
# converting string to integer
number = "14"
int_number = int(number)
print(int_number)

# converting integer to string
jersey_number = 10
str_number = str(jersey_number)
print(str_number)

print("number of letters in your name: " + str(len(input("enter your name: "))))


# number manipulation 
bmi = 84 / 1.65 ** 2
print(bmi)

# rounding a number 
print(round(bmi))
print(round(bmi, 2))

# f-strings
print(f"Your bmi score is {round(bmi, 2)}")

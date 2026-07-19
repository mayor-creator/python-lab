# defining a function
    # def function_name():
        # do something here

def my_function():
    print("Hello")

# calling a function
my_function()

# defining function with parameters
def greeting(name):
    print(f"Hi {name}")
    print(f"How do you do {name}")

# calling function with arguments
greeting("Mayor")
greeting("Jack Sparrow")

# defining function with multiple parameters
def greet_with(name, location):
    print(f"Bonjour {name}, welcome to {location}.")

# calling function with positional arguments
greet_with("Jack Sparrow", "Black Sand Beach")
# calling function with keyword arguments
greet_with(location="New York City", name="Sparrow")

# function with return statement
def format_name(f_name, l_name):
    formatted_name = f"{f_name.title()} {l_name.title()}"
    return formatted_name

print(format_name("mayor", "creator"))
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# function with docstring
def addition(num_1, num_2):
    '''Take two numbers and return the 
    sum of the two numbers'''
    return num_1 + num_2

print(addition(90, 194))
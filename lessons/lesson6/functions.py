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


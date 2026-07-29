# first class functions
def add(a, b):
    return a + b


result = add(3, 4)

print(result)

# assign function to variable without calling it
sum_function = add
print(add)
print(sum_function)
print(sum_function(4, 12))


# passing function as arguments
def double(n):
    return n * 2


def map_function(func, values):
    total = []
    for value in values:
        total.append(func(value))
    return total


double_square = map_function(double, [1, 2, 3, 4, 5])
print(double_square)


# higher order function can:
# 1. take one or more functions as arguments
# 2. return a function as its result
def apply_operation(operation, x, y):
    return operation(x, y)


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


# using higher order function
result_subtract = apply_operation(subtract, 2026, 2012)
result_multiply = apply_operation(multiply, 4, 5)
print(result_subtract)
print(result_multiply)

# lambda functions also known as anonymous functions
# syntax lambda arguments: expression
doubled_values = map_function(lambda n: n * 2, [2, 4, 6, 8, 10])
print(doubled_values)


# closure is an inner function that has access to variables from its
# outer function even after that outer function has completed its
# execution
def outer_scope(name, city):

    def inner_scope():
        print(f"Hello {name.title()}, greetings from {city.title()}.")

    return inner_scope()


# assigning the inner function to a variable
greeting_func = outer_scope(name="juliette", city="paris")
greet = outer_scope("lucas", "lyon")
# calling the inner function
greeting_func
greet

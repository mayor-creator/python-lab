# adding *args and **kwargs to the inner wrapper function.
# inner function now accepts any number of arguments and
# passes them on to the functions that it decorates.

import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        # wrapper function returns the return value of the decorator function
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_hello():
    print("Say hello")


say_hello()


# decorating function with argument
@do_twice
def greet(name):
    print(f"Hello, {name}")


greet("Mayor")


@do_twice
def add_one(number):
    return number + 1


result = add_one(14)
print(result)

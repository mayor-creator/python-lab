from datetime import datetime

# a decorator wraps a function, modifying its behavior


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = decorator(say_whee)
say_whee()


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass

    return wrapper


@not_during_the_night
def say_hi():
    print("Hi!!!")


say_hi()

# exceptions are used to manage errors that arise during a program's execution.
# exceptions are handled with try-except blocks.

# print(5 / 0)

# using try-except block
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by 0!")

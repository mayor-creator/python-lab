def addition(num_1: int, num_2: int):
    """Return the sum of two integers"""
    return num_1 + num_2


try:
    # ask for two numbers then call the addition()
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
except ValueError:
    print("The numbers need to be integers")
else:
    result = addition(first_number, second_number)
    print(result)

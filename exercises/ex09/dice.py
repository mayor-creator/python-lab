from random import choice


def roll_ice(numbers):
    """Return a random number from 6-sided dice"""
    return choice(numbers)


dice = [1, 2, 3, 4, 5, 6]
print(f"You rolled {roll_ice(dice)}")

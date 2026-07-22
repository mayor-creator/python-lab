import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

computer_guess = random.randint(1, 101)
print(computer_guess)

level = input("Choose a difficulty. Type 'easy' or 'hard.': ").lower()
set_guess_count = 10
hard_guess_count = 5
human_guess = 0

def countdown(number):
    result = number -1
    return result

play_game = True
while play_game:
    if level == "easy":
        print(f"You have {set_guess_count} attempts remaining to guess the number.")

        number_guess = int(input("Make guess: "))
        set_guess_count = countdown(set_guess_count)

        if number_guess == computer_guess:
            print("You won")
            play_game = False
        elif number_guess > computer_guess:
            print("Too high")
            print("Guess again")
        else:
            print("Too low")
            print("Guess again")

        if set_guess_count == 0:
            print("GAME OVER YOU LOST!!!")
            play_game = False
    else:
        print(f"You have {hard_guess_count} attempts remaining to guess the number.")

        number_guess = int(input("Make guess: "))
        hard_guess_count = countdown(hard_guess_count)

        if number_guess == computer_guess:
            print("You won")
            play_game = False
        elif number_guess > computer_guess:
            print("Too high")
            print("Guess again")
        else:
            print("Too low")
            print("Guess again")

        if hard_guess_count == 0:
            print("GAME OVER YOU LOST!!!")
            play_game = False
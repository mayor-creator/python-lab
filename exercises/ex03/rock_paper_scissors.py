import random

print("Welcome to the official Rock Paper Scissors Game")
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(human_choice)
computer_choice = random.randint(0, 2)
print(computer_choice)

if human_choice == 0:
    if computer_choice == 1:
        print("Computer Wins")
    elif computer_choice == 0:
        print("Tie Game")
    elif computer_choice == 2: 
        print("You Wins")
elif human_choice == 1: 
    if computer_choice == 0: 
        print("You Wins")
    elif computer_choice == 1: 
        print("Tie Game")
    elif computer_choice == 2: 
        print("Computer Wins")
elif human_choice == 2:
    if computer_choice == 1: 
        print("You Wins")
    elif computer_choice == 2:
        print("Tie Game")
    elif computer_choice == 0: 
        print("Computer Wins")
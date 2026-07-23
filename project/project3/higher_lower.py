import random

from game_data import celebrities

print("HIGHER OR LOWER GAME")
score = 0
play_game = True

while play_game:
    compare_a = random.choice(list(celebrities.values()))
    print(f"\nCompare A: {compare_a["name"].title()}, {compare_a["description"]}")
    print("VS")
    compare_b = random.choice(list(celebrities.values()))
    print(f"Against B: {compare_b["name"].title()}, {compare_b["description"]}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # get instagram followers of compare_a and compare_b
    instagram_a = compare_a["instagram_followers"]
    instagram_b = compare_b["instagram_followers"]

    if choice == "A":
        correct = instagram_a > instagram_b
    elif choice == "B":
        correct = instagram_b > instagram_a
    else:
        print("Invalid choice. Please enter 'A' or 'B'")

    if correct:
        score += 1
        print("Your score is {score}.")
    else:
        play_game = False

print(f"\nGAME OVER. Final Score: {score}.")

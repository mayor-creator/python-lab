import random

word_lists = ['aardvark', "baboon", "camel"]
chosen_word = random.choice(word_lists)
# print(chosen_word)

place_holder = ""
word_length = len(chosen_word)
for letter in range(word_length):
    place_holder += "_"
print(place_holder)

previous_letters = []
lives = 6

start_game = True
while start_game:
    guess = input("Guess a letter of the word: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            previous_letters.append(letter)
        elif letter in previous_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    if guess not in chosen_word:
        lives -= 1
    
    if lives == 0:
        start_game = False
        print("You're hanged. Game over game")

    if "_" not in display:
        start_game = False
        print("You win")
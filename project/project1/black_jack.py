import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#human_list = []
#computer_list = []

#human_choice_1 = random.choice(cards)
#human_choice_2 = random.choice(cards)
#human_list.append(human_choice_1)
#human_list.append(human_choice_2)

#computer_choice_1= random.choice(cards)
#computer_choice_2 = random.choice(cards)
#computer_list.append(computer_choice_1)
#computer_list.append(computer_choice_2)

#human_score = 0
#for i in human_list:
#  human_score += i

#computer_score = 0
#for i in computer_list:
 #   computer_score += i

#if question == 'yes':
#   print(f"Your cards: {human_list}, current score: {human_score}")
#    print(f"Computer's first card: {computer_choice_1}")

#   second_question = input("Type 'yes' to get another card, type 'no' to pass: ")
#    if second_question == 'no':
#        print(f"Your final hand: {human_list}, final score: {human_score}: ")
#       print(f"Computer's final hand: {computer_list}, final score: {computer_score}")

#       if human_score == computer_score:
#           print("Draw Game 😔")
#        elif human_score > 21:
#            print("Computer wins 🏆")
#       else:
#            print("Human wins 🏆")
#   elif second_question == 'yes':
#        human_choice_3 = random.choice(cards)
#       human_list.append(human_choice_1)
#        for i in computer_list:
#            computer_score += i
#        print(f"Your cards: {human_list}, current score: {human_score}")

def deal_card(hand):
    """Add one random card to a hand."""
    hand.append(random.choice(cards))

def calculate_score(hand):
    """Return the total score of a hand."""
    score = 0
    for card in hand:
        score += card
    return score

def show_winner(human_score, computer_score):
    """Display the winner."""
    if human_score == computer_score:
        print("Draw Game 😔")
    elif human_score > 21:
        print("Computer wins 🏆")
    elif computer_score > 21:
        print("Human wins 🏆")
    elif human_score > computer_score:
        print("Human wins 🏆")
    else:
        print("Computer wins 🏆") 

question = (input("Do you want to play a game of Blackjack? Type 'yes' or 'no: "))
target_number = 21

if question == 'yes':
    human_list = []
    computer_list = []

    # starting cards deal
    deal_card(human_list)
    deal_card(human_list)
    deal_card(computer_list)
    deal_card(computer_list)

    human_score = calculate_score(human_list)
    computer_score = calculate_score(computer_list)

    print(f"Your cards: {human_list}, current score: {human_score}")
    print(f"Computer's first card: {computer_list[0]}")

    # Keep asking the player to keep playing until the game is over

    while human_score < target_number:
        second_question = input("Type 'yes' to get another card, type 'no' to pass: ")

        if second_question == 'no':
            break
        deal_card(human_list)
        human_score = calculate_score(human_list)

        print(f"Your cards: {human_list}, current score: {human_score}")

        if human_score > target_number:
           print("You went over 21")
           break

    print(f"Your final hand: {human_list}, final score: {human_score}: ")
    print(f"Computer's final hand: {computer_list}, final score: {computer_score}")

    show_winner(human_score, computer_score)
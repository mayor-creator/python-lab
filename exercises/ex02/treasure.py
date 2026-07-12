print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want ot go?")

direction = input("Type left or right: ")

if direction == "right":
    print("Fall into a hole. GAME OVER.")
elif direction == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("Type wait to wait for a boat. Type swim to swim across. ")
    if choice == "swim":
        print("Attacked by trout. GAME OVER.")
    elif choice == "wait":
        print("Which door will you pick?")
        door = input("Choose red, blue or yellow: ")
        if door == "red":
            print("Burned by fire. GAME OVER.")
        elif door == "blue":
            print("Eaten by beasts. GAME OVER.")
        else: 
            print("YOU WIN ")
        
print("Thank you for playing the Treasure Game!!!")

import json


def get_user_info():
    filename = "python-lab/exercises/ex11/user_info.txt"

    try:
        with open(filename, "r") as file:
            user_info = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        # empty user info list
        user_info = []
        # ask for username
    username = input("What's your name? ").lower()

    # search through the list if the username is found
    for user in user_info:
        if user["name"] == username:
            print(f"Welcome back, {username.title()}")
            print(f"Your favorite number is {user["favorite_number"]}")
            return

    # ask for user favorite number if username is not found
    favorite_number = int(input("Enter favorite number: "))
    # create a new_user_info dictionary
    new_user_info = {"name": username, "favorite_number": favorite_number}
    # add new_user_info to list
    user_info.append(new_user_info)

    with open(filename, "w") as file:
        # save user info
        json.dump(user_info, file, indent=4)
    print(f"Saved information for {username.title()}!")


get_user_info()

filename = "python-lab/lessons/lesson8/guest_names.txt"

ask = True
while ask:
    guest_name = input("Guest names please? or 'q' to end : ")

    # end the prompt
    if guest_name.lower() == "q":
        ask = False
    else:
        # write guest name to a file
        with open(filename, mode="a") as file:
            file.write(f"{guest_name.title()}\n")

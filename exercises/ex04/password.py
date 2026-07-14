import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '#', '$', '%', '*', '&', '*', '(', ')', '+',
]

pick_letters = int(input("How many letters would you like in your password\n"))
password_letters = ""
for letter in range(1, pick_letters + 1):
    random_letters = random.randint(1, len(letters) - 1)
    password_letters += letters[random_letters]

pick_symbols = int(input("How many symbols would you like?\n"))
password_symbol = ''
for symbol in range(1, pick_symbols + 1):
    random_symbol = random.randint(1, len(symbols) - 1)
    password_symbol += symbols[random_symbol]

    
pick_numbers = int(input("How many numbers would you like?\n"))
password_number = ''
for number in range(1, pick_numbers + 1):
    random_numbers = random.randint(1, len(numbers) - 1)
    password_number += numbers[random_numbers]


password = ""
password_list = []
password_list.append(password_letters) 
password_list.append(password_symbol)
password_list.append(password_number)
random.shuffle(password_list)

for char in password_list:
    password += char
print(f"Your new password is {password}")
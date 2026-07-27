# create a list of names
names = ["chloe", "lucas", "juliette", "elise", "antoine"]

# print each name from the list
for name in names:
    print(name)

greeting = ""
# print greeting message for each name
for name in names:
    greeting = f"Salut {name.title()} bienvenue."
    print(greeting)

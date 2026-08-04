# with statement creates a runtime context that allows you
# execute a code block under the control of a context manager

# reading a file
# open() function returns an object representing the file
with open("python-lab/lessons/lesson8/my_file.txt", mode="r") as file:
    content = file.read()

print(content)

# writing to a file
with open("python-lab/lessons/lesson8/new_file.txt", mode="w") as file:
    file.write("Welcome to Paris.\nYou need to visit Louvre Museum before you leave.")

# handling the FileNotFoundError exception
filename = "story.txt"

# utf-8 is encoding argument
try:
    with open(filename, encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
else:
    print(contents)

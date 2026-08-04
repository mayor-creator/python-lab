# read the starting_letter.txt
with open(
    "python-lab/project/project5/input/letters/starting_letters.txt", mode="r"
) as file:
    contents = file.read()

print(contents)

# read each line in invited_names.txt as list item
with open(
    "python-lab/project/project5/input/names/invited_names.txt", mode="r"
) as names_data:
    names = names_data.readlines()


# write a letter for each individual name
for name in names:
    letter_content = contents.replace("Name", name.strip())

    with open(
        f"python-lab/project/project5/output/readyToSend/letter_for_{name.strip()}.txt",
        mode="w",
    ) as file:
        file.write(letter_content)

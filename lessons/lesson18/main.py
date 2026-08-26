from bs4 import BeautifulSoup

filename = "./website.html"

with open(filename) as file_obj:
    contents = file_obj.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)

# find all anchor tags
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# find all the text of the link
for tag in all_anchor_tags:
    print(tag.getText())

# find all links
for tag in all_anchor_tags:
    print(tag.get("href"))

# find an element using the id attribute
heading = soup.find(name="h1", id="name")
print(heading)

# find an element using the class attribute
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# using selectors
name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)

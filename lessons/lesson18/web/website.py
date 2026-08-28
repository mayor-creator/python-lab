from urllib.request import urlopen

from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())

image_links = soup.find_all("img")
print(image_links)

print(soup.title.get_text())
print(soup.title.string)

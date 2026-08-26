import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_webpage_response = response.text

soup = BeautifulSoup(yc_webpage_response, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_text = []
article_tag = []

for article in articles:
    text = article.getText()
    article_text.append(text)

print(article_text)

article_links = soup.select("span a")
for link in article_links:
    article_tag.append(link["href"])

print(article_tag)

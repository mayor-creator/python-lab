import json
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"
page = urlopen(URL)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all(id="zpid_2056905294")
listings = []

for card in cards:
    price = card.find(class_="PropertyCardWrapper__StyledPriceLine")
    address = card.find(name="address")
    link = soup.find("a", class_="StyledPropertyCardDataArea-anchor")

    listings.append(
        {
            "price": int(re.sub(r"[^\d]", "", price.get_text())),
            "address": address.get_text().strip(),
            "link": link["href"],
        }
    )

# for listing in listings:
# currency = f"${listing["price"]:,.2f}"
# print(currency)

filename = "./data/properties.json"
with open(filename, "w") as write_file:
    json.dump(listings, write_file)

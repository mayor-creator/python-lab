import random
from datetime import datetime, timezone

# getting day of the week
now = datetime.now(timezone.utc)
day_of_week = now.weekday()

# read quote file
filename = "python-lab/lessons/lesson12/quotes.txt"
with open(filename, "r") as file:
    quotes = file.readlines()

# picking a random quote from the list
quote = random.choice(quotes)

# check if day is wednesday
if day_of_week == 2:
    print(f"The quote of the day: {quote}")

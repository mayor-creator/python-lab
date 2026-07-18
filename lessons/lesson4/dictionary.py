# create a dictionary ({key: value} pairs)
countries_dictionary = {
    "France": "Paris",
    "Spain": "Madrid",
    "Ghana": "Accra",
    "Japan": "Tokyo"
}

# access an item value from a dictionary
print(countries_dictionary["France"])

# adding an item to a dictionary
countries_dictionary["Egypt"] = "Cairo"
print(countries_dictionary)

# create an empty dictionary
empty_dictionary = {}

# loop through a dictionary
for key in countries_dictionary:
    print(f"Country: {key}")
    print(f"Capital City: {countries_dictionary[key]}")

# nesting a list in dictionary
travel_log = {
    "France": ["Paris", "Lyon", "Lille"],
    "USA": ["New York City", "Los Angeles", "Houston", "New Orleans"],
    "England": ["London", "Liverpool"]
}

# print lyon
lyon_city = travel_log["France"]
print(lyon_city[1])

# nesting a dictionary inside dictionary
travel_log_europe ={
    "France": {
        "cities_visited": ["Paris", "Lyon", "Lille"],
        "total_visited": 3
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 3
    }
}

# print stuttgart
stuttgart_city = travel_log_europe["Germany"]["cities_visited"][-1]
print(stuttgart_city)
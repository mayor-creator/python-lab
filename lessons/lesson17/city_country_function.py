def city_country(city, country, population=""):
    "return the name of a city and country"
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

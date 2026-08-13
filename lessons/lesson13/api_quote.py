import requests

try:
    endpoint = "https://api.kanye.rest/"
    response = requests.get(url=endpoint)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as error:
    print(f"Error occurred: {error}")
else:
    quote = data["quote"]
    print(quote)

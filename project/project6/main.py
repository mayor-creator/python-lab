import datetime

import requests
from user_token import get_token

# api endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# call the token function for unique token
API_TOKEN = get_token()

USERNAME = "creatormayor14"
GRAPH_ID = "graph01"

# username api parameters
user_params = {
    "token": API_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create username
username_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

# create a graph api endpoint
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# graph parameters
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": API_TOKEN}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


# https://pixe.la/v1/users/creatormayor14/graphs

# posting data
post_data_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# get today's date
today_date = datetime.datetime.now()
print(today_date)


# post data parameters
post_data_params = {
    "date": today_date.strftime("%G%m%d"),
    "quantity": input("How many hours did I code today? "),
}

data_response = requests.post(
    url=post_data_endpoint, json=post_data_params, headers=headers
)

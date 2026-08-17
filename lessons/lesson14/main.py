import secrets

import requests

# posting to api
pixela_endpoint = "https://pixe.la/v1/users"

# generate a secure random token
TOKEN = secrets.token_hex(24)
USERNAME = "mayorcreator14"

# user api parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create username with pixela
response = requests.post(url=pixela_endpoint, json=user_params)


# create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph parameters
graph_params = {
    "id": "graph01",
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(graph_response.text)

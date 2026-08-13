import requests

# api request
end_point = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=end_point)
response.raise_for_status()

# accessing api data
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = [longitude, latitude]
print(iss_position)

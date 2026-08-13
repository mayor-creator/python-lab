from datetime import datetime, timezone

import requests

LAT = 38.893452
LNG = -77.014709

# set api parameters
parameters = {"lat": LAT, "lng": LNG, "formatted": 0}

# request an api
endpoint = "https://api.sunrise-sunset.org/json?"
response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()

# access api data
data = response.json()

# using data
sunrise = data["results"]["sunrise"]
print(int(sunrise.split("T")[1].split(":")[0]))
sunset = data["results"]["sunset"]
print(int(sunset.split("T")[1].split(":")[0]))

time_now = datetime.now(tz=timezone.utc)
print(f"Current time: {time_now}")

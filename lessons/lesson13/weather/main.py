import requests

LAT = 38.818125
LON = -77.148380
API_KEY = ""

API_URL = "https://api.openweathermap.org/data/2.5/weather?"


def hourly_forecast_data():
    try:
        parameters = {"lat": LAT, "lon": LON, "appid": API_KEY, "units": "metric"}
        endpoint = API_URL
        response = requests.get(url=endpoint, params=parameters)
        response.raise_for_status()
        forecast_data = response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error occurred {error}")
    else:
        return forecast_data


data = hourly_forecast_data()

print(data)
print(data["name"])

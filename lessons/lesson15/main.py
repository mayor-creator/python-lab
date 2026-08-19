import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")


API_URL = "https://app.100daysofpython.dev"
POST_URL = "/v1/nutrition/natural/exercise"

HEADERS = {"x-app-id": APP_ID, "x-app-key": API_KEY}

exercise_parameters = {"query": input("Tell me which exercises you did?: ")}

response = requests.post(
    url=f"{API_URL}{POST_URL}", json=exercise_parameters, headers=HEADERS
)

data = response.json()


def get_exercise():
    for item in data["exercises"]:
        exercise = item["name"]
    return exercise.title()


def get_duration():
    for item in data["exercises"]:
        duration = item["duration_min"]
    return duration


def get_calories():
    for item in data["exercises"]:
        calories = item["nf_calories"]
    return calories


today = datetime.datetime.now()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%H:%M:%S")

EXERCISE = get_exercise()
DURATION = get_duration()
CALORIES = get_calories()

SHEETY_KEY = os.getenv("SHEETY_KEY")
SHEETY_API = f"https://api.sheety.co/{SHEETY_KEY}/pythonWorkoutTracking/workouts"

exercise_data = {
    "date": DATE,
    "time": TIME,
    "exercise": EXERCISE,
    "duration": DURATION,
    "calories": CALORIES,
}

body = {"workout": exercise_data}

HEADER_KEY = os.getenv("HEADER_KEY")
headers = {"Authorization": HEADER_KEY}

sheety_response = requests.post(url=SHEETY_API, json=body, headers=headers)
# print(sheety_response.text)

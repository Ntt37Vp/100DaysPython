import requests
import os
import datetime as dt
import json


# Ask user input
exercises = input("Tell me the exercises you did ")

# Constants
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_PARAMS = {
    "query": exercises,
}
NUTRI_APP_KEY = os.environ.get("NUTRI_APP_KEY")
NUTRI_HEADERS = {
    "x-app-id": "f6026853",
    "x-app-key": NUTRI_APP_KEY
}
SHEETY_ENDPOINT = "https://api.sheety.co/d058581b665d834a29813c71c35e3681/myWorkouts/workouts"
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_HEADERS = {
    "Authorization": SHEETY_AUTH
}
# Get data from Nutritionix
response = requests.post(url=NUTRI_ENDPOINT, json=NUTRI_PARAMS, headers=NUTRI_HEADERS)
exercise = response.json()["exercises"][0]["name"]
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]
date_entry = str(dt.datetime.now().date())
time_entry = str(dt.datetime.now().time())
workoutToParse = {
    "workout": {
        "date": date_entry,
        "time": time_entry,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}
# Parse into SHEETY
for_sheety = requests.post(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS, json=workoutToParse)
for_sheety.raise_for_status()
print(for_sheety.status_code)

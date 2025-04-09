import os
import requests
# from requests.auth import HTTPBasicAuth
from datetime import datetime

APP_ID = os.environ["NUTRITIONIX_APP_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY"]
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/9a30d3187742b0873fb915d9cab40aed/hamza'sWorkouts/workouts"

user_input = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": user_input,
}

exercise_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_parameters, headers=headers)
exercise_data = exercise_response.json()


today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

sheety_headers = {
    "Authorization": f"Bearer {os.environ.get["SHEETY_TOKEN"]}"
}

for exercise in exercise_data["exercises"]:

    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"]),
            "calories": round(exercise["nf_calories"]),
        }
    }

    # basic = HTTPBasicAuth(os.environ.get["SHEETY_USERNAME"], os.environ.get["SHEETY_PASSWORD"])
    # sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, auth=basic)
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
    print(sheety_response.text)

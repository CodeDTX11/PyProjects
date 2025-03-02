import requests
import os
from datetime import datetime

### IMPORTANT: must run workout_tracker configuration to access environment variables

# APP_ID_NUTRITIONIX= "48bf2799"
# API_KEY_NUTRITIONIX = "db7ab5ddf2b83244dfdef6de486e0f82"

# BEARER_TOKEN_SHEETY = "9oilkakfds3rj343km4k2k3mdfs09df8f9"

APP_ID_NUTRITIONIX = os.environ.get("APP_ID_NUTRITIONIX")
API_KEY_NUTRITIONIX = os.environ.get("API_KEY_NUTRITIONIX")
BEARER_TOKEN_SHEETY = os.environ.get("BEARER_TOKEN_SHEETY")

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 170
AGE = 33

exercise_nutritionix_endpt = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrition_headers = {
    "x-app-id" : APP_ID_NUTRITIONIX,
    "x-app-key" : API_KEY_NUTRITIONIX
}

# u_input = input("What exercise did you do? ")
u_input = "cycled for 10 minutes and hiked for 1 hour"

parameters = {
    "query" : u_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
exercise_response = requests.post(url=exercise_nutritionix_endpt, json=parameters, headers=nutrition_headers)

# print(exercise_response.json())

exercise_response_data = exercise_response.json()

post_sheety_endp = "https://api.sheety.co/4b4b124370147e209a1f2e0c2bd5884f/myWorkoutTracker/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_inputs= {}

sheety_headers = {
    "Authorization" : f"Bearer {BEARER_TOKEN_SHEETY}"
}

for exercise in exercise_response_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(url=post_sheety_endp, json=sheet_inputs, headers=sheety_headers)
    print(sheety_response)
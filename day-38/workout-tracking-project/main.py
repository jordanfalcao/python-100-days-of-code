import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 76
HEIGHT_CM = 171
AGE = 32
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# environments variables
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

parameters = {
    "query": input("Which exercise did you do today: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

header_parameters = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# post the exercise with NLP
response = requests.post(url=EXERCISE_ENDPOINT, headers=header_parameters, json=parameters)
results = response.json()

#####################################################
headers_sheety = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# loop to set all the exercises day
for exercise in results['exercises']:
    today = datetime.now()
    formatted_hour = today.strftime("%X")
    formatted_date = today.strftime("%m/%d/%Y")

    # inputs to set in google sheet in json
    sheet_inputs = {
        "workout": {
            "date": formatted_date,
            "time": formatted_hour,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    # set in the Google sheet with Sheety
    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=headers_sheety)

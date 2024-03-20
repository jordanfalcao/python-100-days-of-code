import requests

APP_ID = "your app id"  # SET YOUR APP ID HERE
API_KEY = "you app key"  # SET YOUR APP KEY HERE
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": input("Which exercise did you do today: "),
    "gender": "male",
    "weight_kg": 76,
    "height_cm": 171,
    "age": 32
}

header_parameters = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=ENDPOINT, headers=header_parameters, json=parameters)
result = response.json()
print(result)

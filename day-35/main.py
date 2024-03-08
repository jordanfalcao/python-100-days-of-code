import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "set-your-api-key-here"  # SET YOUR OWN API KEY HERE

parameters = {
    'lat': -7.040262,
    'lon': -34.843010,
    'appid': api_key
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

print(data)
import requests
import os
from twilio.rest import Client


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your-api-key-here"  # SET YOUR OWN API KEY HERE

account_sid = "your-twilio-account-sid-here"  # account SID from Twilio console
auth_token = "your-twilio-auth-token-here"  # auth Token from Twilio console

parameters = {
    'lat': -7.040262,
    'lon': -34.843010,
    'appid': api_key,
    'cnt': 4,  # just next 12 hours
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour in data['list']:
    if hour['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_="twilio-phone-number",  # your Twilio phone number
        to="phone-to-text"  # your verified number set on Twilio
    )
    print(message.status)

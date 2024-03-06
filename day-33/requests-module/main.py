import requests
from datetime import datetime

MY_LAT = -6.980210
MY_LONG = -34.830360

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# # print(response.text)
# # print(response.status_code)
#
# response.raise_for_status()  # get any error and raise it
#
# data = response.json()
# print(data['iss_position']['latitude'])
#
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
#
# iss_position = (latitude, longitude)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
    'tzid': "America/Recife"
}

response = requests.get('https://api.sunrise-sunset.org/json',
                        params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]  # get the hour
sunset = data['results']['sunset'].split("T")[1].split(":")[0]  # get the hour

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
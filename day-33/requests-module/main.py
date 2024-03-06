import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response.text)
# print(response.status_code)

response.raise_for_status()  # get any error and raise it

data = response.json()
print(data['iss_position']['latitude'])

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_position = (latitude, longitude)
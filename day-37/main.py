import requests
from datetime import datetime

USERNAME = "youruser"  # set your Pixela username here
TOKEN = "yourtoken"  # set your Pixela token here

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,  # password-manager-tkinter: data.json
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # keep commented since the user was created
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_parameters = {
    "id": "python100graph",
    "name": "Programming Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# # keep commented since the graph was created
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_parameters = {
    "date": today.strftime("%Y%m%d"),  # formatted in yyyyMMdd
    "quantity": "3.5"
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/python100graph"
# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
# print(response.text)

update_parameters = {
    "quantity": "4.5"
}

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/python100graph/{today.strftime('%Y%m%d')}"
response = requests.post(url=pixel_update_endpoint, json=update_parameters, headers=headers)
print(response.text)
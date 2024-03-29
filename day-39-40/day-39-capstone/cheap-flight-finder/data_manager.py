import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ['SHEETY_PRICES_ENDPOINT']
SHEETY_USERS_ENDPOINT = os.environ['SHEETY_USERS_ENDPOINT']
BEARER = os.environ['BEARER']

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.parameters = {}
        self.destination_data = {}
        self.users_data = {}
        self.headers = {"Authorization": f"Bearer {BEARER}"}

    def get_data(self):
        sheet_response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = sheet_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def write_row(self):
        self.parameters = {
            "price": {
                "city": input("Enter city name: ").title(),
                "iataCode": input("Enter iata code: ").upper(),
                "lowestPrice": input("Enter lowest price: ")
            }

        }
        write_response = requests.post(url=SHEETY_PRICES_ENDPOINT, json=self.parameters)

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_users_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        self.users_data = data["users"]
        return self.users_data

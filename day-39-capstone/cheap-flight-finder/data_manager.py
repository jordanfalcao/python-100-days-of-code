import requests
import os

SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.parameters = {}
        self.destination_data = {}

    def get_data(self):
        sheet_response = requests.get(url=SHEET_ENDPOINT)
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
        write_response = requests.post(url=SHEET_ENDPOINT, json=self.parameters)

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
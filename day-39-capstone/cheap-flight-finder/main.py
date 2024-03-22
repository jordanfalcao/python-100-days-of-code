# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import TEQUILA_API_KEY
from pprint import pprint

data_manager = DataManager()  # initiating DataManager class
sheet_data = data_manager.get_data()  # getting destination data from sheet
print(sheet_data[0])

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    pprint(f"sheet_data:\n{sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()  # initiating DataManager class
# data_manager.write_row()
sheet_data = data_manager.get_data()  # getting destination data from sheet
flight_search = FlightSearch()  # initiating FlightSearch class

# filling sheet if IATA Code is empty
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# date variables
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )

# headers = {"apikey": TEQUILA_API_KEY}
# query = {
#     "fly_from": ORIGIN_CITY_CODE,
#     "fly_to": "PAR",
#     "date_from": "2021",
#     "date_to": "2021-05-01",
#     "nights_in_dst_from": 7,
#     "nights_in_dst_to": 28,
#     "max_stopovers": 0,
#     "curr": "GBP"
# }
# response = requests.get(
#     url=f"{TEQUILA_ENDPOINT}/v2/search",
#     params=query,
#     headers=headers
# )
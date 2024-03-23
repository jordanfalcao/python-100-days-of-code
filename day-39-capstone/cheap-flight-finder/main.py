from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()  # initiating DataManager class
# data_manager.write_row()
sheet_data = data_manager.get_data()  # getting destination data from sheet
flight_search = FlightSearch()  # initiating FlightSearch class
notification = NotificationManager()  # initiating NotificationManager class

# fills the sheet if IATA Code is empty
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# date variables
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

# loop through sheet and storage the lowest price for each city
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )
    # checks if the lowest price found is less than the lowest historical price
    if flight.price < destination['lowestPrice']:
        notification.send_notification(f"Low price ALERT! Only £{flight.price} to fly from "
                                       f"{flight.origin_city}-{flight.origin_airport} to "
                                       f"{flight.destination_city}-{flight.destination_airport}, "
                                       f"from {flight.out_date} to {flight.return_date}.")

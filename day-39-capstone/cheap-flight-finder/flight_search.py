import requests
import os

TEQUILA_ENDPOINT = ""
TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']



class FlightSearch:
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code

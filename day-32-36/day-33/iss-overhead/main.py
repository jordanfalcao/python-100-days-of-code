import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -6.980210
MY_LONG = -34.830360
MY_EMAIL = "youremailhere@gmail.com"  # CHANGE TO YOUR EMAIL HERE
PASSWORD = "apppasswordhere"  # CHANGE TO THE APP PASSWORD HERE


def iss_overhead():
    """Returns True if ISS is overhead your position."""
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    """Returns True if is night in your position"""
    parameters = {  # parameters to set in next request
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        'tzid': "America/Recife"  # UTC-3 in order to adjust the time
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # get the hour
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # get the hour

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(90)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, to_addrs="emailtosend@yahoo.com",
                msg="Subject: ISS Alert!\n\nThe ISS is above you in the sky and"
                    "is night. Go look up!"
            )

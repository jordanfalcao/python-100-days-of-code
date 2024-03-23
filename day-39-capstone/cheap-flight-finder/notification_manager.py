from twilio.rest import Client
import os

ACCOUNT_SID = os.environ['ACCOUNT_SID']  # account SID from Twilio console
AUTH_TOKEN = os.environ['AUTH_TOKEN']  # auth Token from Twilio console
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
MY_NUMBER = os.environ['MY_NUMBER']


class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_=TWILIO_NUMBER,  # your Twilio phone number
            to=MY_NUMBER  # your verified number set on Twilio
        )
        print(message.status)

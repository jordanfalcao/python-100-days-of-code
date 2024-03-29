from twilio.rest import Client
import smtplib
import os

ACCOUNT_SID = os.environ['ACCOUNT_SID']  # account SID from Twilio console
AUTH_TOKEN = os.environ['AUTH_TOKEN']  # auth Token from Twilio console
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
MY_NUMBER = os.environ['MY_NUMBER']

MY_EMAIL = os.environ['MY_EMAIL']
TO_EMAIL = os.environ['TO_EMAIL']
APP_PASSWORD = os.environ['APP_PASSWORD']


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

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: Low Price Flight!!\n\n{message}".encode('utf-8')
                )

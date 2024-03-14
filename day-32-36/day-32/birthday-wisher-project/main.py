import smtplib
import random
import datetime as dt
import pandas as pd
import os

##################### Extra Hard Starting Project ######################
my_email = "your_email_here@gmail.com"  # CHANGE TO YOUR EMAIL HERE
password = "apppasswordhere"  # CHANGE TO THE APP PASSWORD HERE

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
data_list = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
# 3. Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

today = dt.datetime.now()  # today date

# check if today is someone birthday
for item in data_list:
    if item["month"] == today.month and item["day"] == today.day:
        letter = random.choice(os.listdir("letter_templates"))

        with open(f"letter_templates/{letter}", "r") as file:
            content = file.read()

        new_content = content.replace("[NAME]", item["name"])

        # send email with smtp
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, to_addrs=item["email"],
                msg=f"Subject: Happy Birthday!\n\n{new_content}"
            )

# import smtplib
#
# my_email = "jordan.python.bootcamp@gmail.com"
# password = "usemyapppassword"  # CHANGE TO THE APP PASSWORD HERE
#
# # create  SMTP object
# with smtplib.SMTP('smtp.gmail.com') as connection:  # for gmail
#     connection.starttls()  # Transport Layer Security: encript message
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, to_addrs="jordan.python@yahoo.com",
#         msg="Subject: Email with Python\n\nHello, this is a Python message."
#     )
# # connection.close()  # avoid use it by usgin 'with' key


# ----------------------------------------DATETIME---------------------------------------- #
import datetime as dt

now = dt.datetime.now()  # return 'year-month-day hh:mm:ss.accacc'

# now.year
# now.month
# now.day
# now.hour
# now.minute
# now.second
day_of_week = now.weekday()
print(day_of_week)

# create my own datetime object
date_of_birth = dt.datetime(year=1991, month=10, day=28)
print(date_of_birth)
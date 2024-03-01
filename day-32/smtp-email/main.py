import smtplib

my_email = "jordan.python.bootcamp@gmail.com"
password = "usemyapppassword"  # CHANGE TO THE APP PASSWORD HERE

# create  SMTP object
with smtplib.SMTP('smtp.gmail.com') as connection:  # for gmail
    connection.starttls()  # Transport Layer Security: encript message
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, to_addrs="jordan.python@yahoo.com",
        msg="Subject: Email with Python\n\nHello, this is a Python message."
    )
# connection.close()  # avoid use it by usgin 'with' key
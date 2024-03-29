from sheety import post_new_row

print("""
  Welcome to Jordan's Flight Club!
  We find the best flight deals and email you.
""")

first_name = input("What's your first name? ").title()
last_name = input("What's your last name? ").title()

email1 = "1"
email2 = "2"

while email1 != email2:
    email1 = input("What's your email? ")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()

    email2 = input("Type your email again. ")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()

print("You're in the club!")

# Sheety API
post_new_row(first_name, last_name, email1)

# TIP CALCULATOR

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇

print("Welcome to the tip calculator!")
# input variables
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

# coverting variables
bill_float = float(bill)
tip_float = float(tip)
people_int = int(people)

# tip percent
tip_float = (tip_float / 100) + 1


total_bill = bill_float * tip_float
split_bill = total_bill / people_int

rounded_split_bill = round(split_bill, 2)

print(f"Each person should pay: ${rounded_split_bill:.2f}")
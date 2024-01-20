from replit import clear
from art import logo    # import logo from art.py

print(logo)
print("Welcome to the secret auction program.")

bid_dict = {} # create dict

continue_input = True
# while loop to continue until ask_input = 'no'
while continue_input:
  name = input("What is your name: ")  # name input
  bid_price = input("What is your bid price: $")   # bid input
 
  bid_dict[name] = bid_price   # add name key and bid_price value to dictionary  
  # 'yes' or 'no'
  ask_input = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  
  if ask_input == "yes":
    clear()
  elif ask_input == "no":
    continue_input = False

# looping for checking which is the highest bid
highest_bid = 0
for key in bid_dict:
  interger_key = int(bid_dict[key])
  if interger_key > highest_bid:
    highest_bid = interger_key
    winner = key


print(f"The winner is {winner} with a bid of {highest_bid}")
  
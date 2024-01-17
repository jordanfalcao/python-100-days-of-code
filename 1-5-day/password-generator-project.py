#Password Generator Project

## COMMOM CODE FOR THE 3 RESOLUTIONS:
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

###################################################################################33
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# # loop to insert random letters, symbols and numbers in SEQUENTIAL order
# for letter in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for symbol in range (1, nr_symbols + 1):
#   password += random.choice(symbols)

# for number in range (1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(f"\nHere is your password: {password}")


#############################################################################################################################
#HARD LEVEL - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# # iniating counter variables
# count_letter = nr_letters
# count_symbols = nr_symbols
# count_number = nr_numbers

# # total counter
# countpass = nr_letters + nr_symbols + nr_numbers
# password = ""

# # loop to insert random letters, symbols and numbers in RANDOM order
# for count in range(1, countpass + 1):
#     if count_letter != 0 and count_symbols != 0 and count_number != 0:    # if all counters are not 0
#         int_random = random.randint(1, 3)

#          # inserting random LETTER or SYMBOL or NUMBER and decreasing the respective counter by 1
#         if int_random == 1:
#             password += random.choice(letters)
#             count_letter -= 1
#         elif int_random == 2:
#             password += random.choice(symbols)
#             count_symbols -= 1
#         else:            
#             password += random.choice(numbers)
  #           count_number -= 1

  # #   inserting random LETTER or SYMBOL and decreasing the respective counter by 1
  #   elif count_letter != 0 and count_symbols != 0:        
  #       int_random = random.randint(1, 2)

  #       if int_random == 1:
  #           password += random.choice(letters)
  #           count_letter -= 1
  #       else:
  #           password += random.choice(symbols)
#             count_symbols -= 1

  # #   inserting random LETTER or NUMBER and decreasing the respective counter by 1
#     elif count_letter != 0 and count_number != 0:        
#         int_random = random.randint(1, 2)

#         if int_random == 1:
#             password += random.choice(letters)
#             count_letter -= 1
#         else:
#             password += random.choice(numbers)
#             count_number -= 1

#     #   inserting random SYMBOL or NUMBER and decreasing the respective counter by 1
#     elif count_symbols != 0 and count_number != 0:        
#         int_random = random.randint(1, 2)

#         if int_random == 1:
#             password += random.choice(symbols)
#             count_symbols -= 1
#         else:
#             password += random.choice(numbers)
#             count_number -= 1

#     #   inserting random LETTER and decreasing the respective counter by 1
#     elif count_letter != 0:        
#         password += random.choice(letters)
#         count_letter -= 1

#     #   inserting random SYMBOL and decreasing the respective counter by 1
#     elif count_symbols != 0:        
#         password += random.choice(symbols)
#         count_symbols -= 1
#     else:                     #   inserting random NUMBER and decreasing the respective counter by 1
#         password += random.choice(numbers)
#         count_number -= 1


# print(f"\nHere is your password: {password}")

##############################################################################################
#HARD LEVEL - Order of characters randomised: OTHER METHOD

password_list = []
password = ""

# same loop from the 1st resolution, but instead of adding to the password string, add to the password_list
for letter in range(1, nr_letters + 1):
  password_list += random.choice(letters)

for symbol in range (1, nr_symbols + 1):
  password_list += random.choice(symbols)

for number in range (1, nr_numbers + 1):
  password_list += random.choice(numbers)

total = nr_letters + nr_symbols + nr_numbers

# randomize the order of the list and convert it to a string
for count in range(1, total + 1):
  int_random = random.randint(0, len(password_list) - 1)
  password += password_list.pop(int_random)


print(f"\nHere is your password: {password}")
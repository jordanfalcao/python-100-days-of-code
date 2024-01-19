# lowercase alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# creating Caesar Function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""   # initiating end_text as empty string
  if cipher_direction == "decode":    # if decode, shift_amount is negative 
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:                                         # IF char is in alphabet list: do the logic\
      position = alphabet.index(char)                            #                                           \
      new_position = position + shift_amount                     #                                             \
      if new_position > 25 or new_position < 0: # if new position out of range, get the module                 /
        new_position = new_position % 26                         #                                            /
      end_text += alphabet[new_position]                         #                                           /
    else:                                                        # ELSE, just add the char to end_text      /
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

# while loop to continue the program
continue_question = True
while continue_question:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))  

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  # Ask the user if they want to restart the cipher program and set the continue_question to True or False
  continue_question = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if continue_question == "no":
    continue_question = False
    print("Goodbye. Thank you for using Caesar Cipher.")
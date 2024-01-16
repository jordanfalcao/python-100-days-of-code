# Rock Paper Scissors
# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable:
# rock, paper, and scissors. This will make it easy to print them out to the console.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
# You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random # import module

# input to integer
input_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# print input choice 
if input_rps == 0:
  print(rock)
elif input_rps == 1:
  print(paper)
else:
  print(scissors)

# random computer choice
computer_coice = random.randint(0, 2)
print("Computer chose:")

# print computer choice
if computer_coice == 0:
  print(rock)
elif computer_coice == 1:
  print(paper)
else:
  print(scissors)

# compare which one wins
if input_rps == 0 and computer_coice == 2:
  print("You win!!!")
elif input_rps == 1 and computer_coice == 0:
  print("You win!!!")
elif input_rps == 2 and computer_coice == 1:
  print("You win!!!")
elif input_rps == computer_coice:
  print("It's a draw!")
else:
  print("You lose!!")


###############################################################
#### IMPROVING THE CODE
### DEBUG INVALID NUMBER ERROR
### NEW INDEX METHOD

  rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# new index
images = [rock, paper, scissors]

# input to integer
input_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# debugging invalid number error
if input_rps >= 3 or input_rps < 0:
  print("You typed an invalid number, you lose!")
else:
  print(images[input_rps])  # print IMAGES list according INPUT INDEX
  
  computer_coice = random.randint(0, 2)
  print("Computer chose:")
  print(images[computer_coice]) #print IMAGES list according COMPUTER INDEX
  
  if input_rps == 0 and computer_coice == 2:
    print("You win!!!")
  elif input_rps == 1 and computer_coice == 0:
    print("You win!!!")
  elif input_rps == 2 and computer_coice == 1:
    print("You win!!!")
  elif input_rps == computer_coice:
    print("It's a draw!")
  else:
    print("You lose!!")
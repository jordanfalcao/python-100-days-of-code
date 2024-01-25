#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

# decreaing the number of attempts or print you win
def guess_func(guess, answer, turns):
  if guess == answer:
    print(f"You got it! The answer was {answer}!!")    
  elif guess < answer:
    print("Too low.\n")
    return turns - 1
  else:
    print("Too high.\n")
    return turns - 1

# iniciate the game
def game():
  print(logo)
  print("\nWelcome to the Number Guessing Game!!!")
  print("I'm thinking of a number between 1 and 100.")
  chosen_number = random.randint(1, 100)
  # print(f"Pssst, the correct answer is {chosen_number}")

  # sets the difficulty to take the num of attempts
  level_turns = 0
  if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    level_turns = 10
  else:
    level_turns = 5

  guess = 0
  while guess != chosen_number:
    print(f"You have {level_turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    level_turns = guess_func(guess, chosen_number, level_turns)

    # if the user runs out of attempts or try again
    if level_turns == 0:
      print("You lose")
      return
    elif guess != chosen_number:
      print("Guess again.")
  
# calliing the game function
game()

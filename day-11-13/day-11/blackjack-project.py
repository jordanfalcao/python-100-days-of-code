############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from replit import clear
from art import logo

# function to deal cards from a list
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
  card = random.choice(cards)
  return card

# function to calculate the score of a list of cards
def calculate_score(cards_list):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards_list) == 21 and len(cards_list) == 2:
    return 0

  if 11 in cards_list and sum(cards_list) > 21:
    cards_list.remove(11)
    cards_list.append(1)
    
  return sum(cards_list)

def compare_cards (user_score, computer_score):
  """Compare cards and return the winner"""
  if user_score == computer_score:
    return "Draw 🙃."     
  elif computer_score == 0:
    return "Lose, opponent has Blackjack!!! 😱"
  elif user_score == 0:
    return "Win with a Blackjack!!! 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

# function to play the game
def play_game():
  """Deal cards and play the game"""
  print(logo)

  # initialize the user and computer cards
  user_cards = []
  computer_cards = []

  # deal the first two cards to each one
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  # while loop to keep asking the user if they want to draw another card
  continue_game = True
  while continue_game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)  
  
    print(f"Your cards: {user_cards}, current score: {user_score}.")
    print(f"Computer's first card: {computer_cards[0]}.\n")

    # check if the user or computer has a blackjack or if the user has gone over 21
    if user_score == 0 or computer_score == 0 or user_score > 21:
      continue_game = False  # ending picking card
    else:
      if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
        user_cards.append(deal_card())
      else:
        continue_game = False  # ending picking card

  # IF clause to fix the bug where the computer can pick another card after the user has gone over 21
  if user_score <= 21 and user_score != 0: 
    while computer_score != 0 and computer_score < 17:  # while loop to keep picking cards for the computer
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

  print(f"\nYour final hand: {user_cards}, final score: {user_score}.")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
  
  print(compare_cards(user_score, computer_score))

# while loop to keep playing the game
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()

import random
from game_data import data
from art import logo, vs
from replit import clear

### Higher or Lower Game ###

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def get_data_info(account):
  """Format account into printable format: name, description and country"""
  name = account['name']
  description = account['description']
  country = account['country']

  return f"{name}, a {description}, from {country}"

# creating game function
def game():
  print(logo)
  account_b = get_random_account() # initiating account_b
  should_continue = True            
  score = 0
    
  # while looping until shoul_continue is True
  while should_continue:
    account_a = account_b
    account_b = get_random_account()
    a_followers = account_a['follower_count'] # getting followers for account_a
    b_followers = account_b['follower_count'] # getting followers for account_b

    print(f"Compare A: {get_data_info(account_a)}.")
    print(vs)
    print(f"Against B: {get_data_info(account_b)}.\n")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check_answer(guess, account_a['follower_count'], account_b['follower_count'])
    if guess == 'a' and a_followers > b_followers:
      score += 1
      print(f"You're right! Current score: {score}.\n")
    elif guess == 'b' and b_followers > a_followers:
      score += 1
      print(f"You're right! Current score: {score}.\n")
      return score
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}.")
      should_continue = False

# calling game function
game()
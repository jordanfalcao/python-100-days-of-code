from game_data import data
import random
from art import logo, vs

### Higher or Lower Game ###

def get_random_account(list):
  return random.choice(list)

def get_data_info(account):
  name = account['name']
  description = account['description']
  country = account['country']

  return f"{name}, a {description}, from {country}"

# aleatory = random.choice(data)
# print(get_data_info(aleatory))

def check_answer(guess, a_followers, b_followers):
  score = 0
  right_answer = True
  while right_answer:
    if guess == 'a' and a_followers > b_followers:
      score += 1
      print(f"You're right! Current score: {score}.")
    elif guess == 'b' and b_followers > a_followers:
      score += 1
      print(f"You're right! Current score: {score}.")
      return score
    else:
      print(f"Sorry, that's wrong. Final score: {score}.")
      right_answer = False


check_answer('a', 20, 10)

# def game():
#   print(logo)
#   account_a = get_random_account()
#   account_b = get_random_account()
#   should_continue = True
#   score = 0
#   while should_continue:
#     account_a = account_b
#     account_b = get_random_account()
#     print(f"Compare A: {get_data_info(account_a)}.\n")
#     print(vs)
#     print(f"Compare A: {get_data_info(account_b)}.\n")
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#     check_answer(guess, account_a['follower_count'], account_b['follower_count'])


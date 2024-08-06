# display art

# generate random account from the game data

# format the data into a printable format. make it look nice

# asks for a guess to the user

# checks if the user choice is correct. will compare the follower count between the users

# give the user feedback

# save the score

# the game starts again

#the next game starts with the account that won but it becomes the accoubnt at position A.

# doesnot clutter the screen . clear everything and displays again

# display art
from art2 import logo,vs
from game_data import data
import random


def formatData(account):
  # format the data into a printable format. make it look nice
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]

  return (f"{account_name}, a {account_desc}, from {account_country}")



def check_answer(user_guess, a_follower, b_follower):
  if a_follower > b_follower:
    return user_guess == "a"
  else:
    return user_guess == "b"





score = 0
game_should_go_on = True
account_b = random.choice(data)


while game_should_go_on:
  print(logo)
  
  # generate random account from the game data
  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A : {formatData(account_a)}.")
  print(vs)
  print(f"Compare B : {formatData(account_b)}.")
  
  # asks for a guess to the user
  
  guess= input("Guess who has more followers? A or B: ").lower()
  
  print("\n" *20) #prints 20 empty lines
  
  print(logo)
  
  # checks if the user choice is correct. will compare the follower count between the users
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  # give the user feedback
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
   
  if is_correct:
    score += 1
    print("You are right!")
  else: 
    print("your dumb!")
    game_should_go_on = False
  

  
  
  
  


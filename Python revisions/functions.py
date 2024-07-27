

def prime_checker(number):
  is_prime = True
  for n in range(2,number):
    if (number%n == 0):
      is_prime = False
  if (is_prime == True):
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    


##################################################################################################################################


n = int(input()) 
prime_checker(number=n)


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(plain_text, shift_amount):

    cipher_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        new_positon = position + shift
        new_letter = alphabet[new_positon]

        cipher_text = cipher_text + new_letter
    print(f"Your encoded text is {cipher_text}")


def decrypt(cypher_text, shift_amount):
    plain_text = ""
    alphabet.reverse()
    for letter in cypher_text:
        position = alphabet.index(letter)
        new_positon = position + shift
        new_letter = alphabet[new_positon]

        plain_text = plain_text + new_letter
    print(f"Your encoded text is {plain_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if (direction == "encode"):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)

elif (direction == "decode"):
    cypher = input("Enter the text you want to decode\n".lower())
    shift = int(input("Type the shift number:\n"))
    decrypt(cypher, shift)
else:
    print("Wrong choice. choose between 'encode' and 'decode'\n")


################################################################################






programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}


# key and value. 
# define by  == dictionary name = { key : value, 
#                                    key : value, key:value}

# add === dictionary_name[key] = value //// This will ad a new value at the last 
# delete dictionary == dictionary_name = {} //// this deletes teh whole dict.
# change value === dictionary_name[existing key] = new value

# keys and value can be string or int whatever 

# LOOP through dictionary 

for i in programming_dictionary:
  print(i)  #this gives us all the keys 
  print(programming_dictionary[i]) # this gives us key values 


print(programming_dictionary["Bug"]) # will print the value for BUG key. 


###################################################################################


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for i in student_scores:
  if (student_scores[i] >= 91 and student_scores[i] <= 100):
    student_grades[i] = "Outstanding"
  elif (student_scores[i] >= 81 and student_scores[i] <= 90):
    student_grades[i] = "Exceeds Expectations"
  elif (student_scores[i] >= 71 and student_scores[i] <= 80):
    student_grades[i] = "Acceptable"    
  elif (student_scores[i] <= 70):
    student_grades[i] = "Fail" 


print(student_grades)



########################################################################################

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


#function that will allow new countries
# to be added to the travel_log.

def add_new_country(new_country, new_visits, new_cities):
 #to add a new disctionary to the list we have to create a dictionary manually. 
  # there is nbo way to refer a key of a dictionary that is inside a list. 
  # so we make a dictionary and than append the new dictionary to the list. 

  new_dictionary = {}
  new_dictionary["country"] = new_country
  new_dictionary["visits"] = new_visits
  new_dictionary["cities"] = new_cities

  travel_log.append(new_dictionary)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")



###########################################################################################################


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  
  if (month == 2 and is_leap(year)):
    print(f"leap year {month_days[1] +1} days")
  else:
    print(f"Not leap year {month_days[month-1]} days")
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

############################################################################################################

# calculator


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
#we will use the dict to call functions

num1 = int(input("Whats the first number?\n"))
num2 = int(input("Whats the second number?\n"))

for key in operations:
  print(key)
choose = input("pick a operation from the lines above.\n")

calculation_funct = operations[choose]
#we are storing user choice in a variable.
#lets say the user chose ADD
#Now calculation funct value is add.

answer = calculation_funct(num1, num2)
#this line is same as writing  -- add(num1,num2) --we just called the functon

print(f"{num1} {choose} {num2} = {answer}")


#################################################################################### flag and while loops ################################

# calculator


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
#we will use the dict to call functions

num1 = int(input("Whats the first number?\n"))
num2 = int(input("Whats the second number?\n"))

for key in operations:
  print(key)
  
should_continiue = True


  
choose = input("pick a operation from the lines above.\n")

calculation_funct = operations[choose]
#we are storing user choice in a variable.
#lets say the user chose ADD
#Now calculation funct value is add.

answer = calculation_funct(num1, num2)
#this line is same as writing  -- add(num1,num2) --we just called the functon

print(f"{num1} {choose} {num2} = {answer}")


#####################################################################################################################################

# calculator - FLAGS AND WHILE LOOPS TO KEEP IT RUNNING
 

def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
#we will use the dict to call functions

num1 = int(input("Whats the first number?\n"))
#in a calculator, you ask for the first number only once.

should_continue = True
while should_continue:

  num2 = int(input("Whats the next number?\n"))

  for key in operations:
    print(key)
  choose = input("pick a operation from the lines above.\n")
  calculation_funct = operations[choose]
  answer = calculation_funct(num1, num2)
  print(f"{num1} {choose} {num2} = {answer}")

  if (input(f"Type 'y' to continue or type 'n' to stop\n") == 'y'):
    num1 = answer
    #in a calculator, the previous answer is the first number of second opearation
  else:
    should_continue = False


################################################################################################################################
 
# calculator - WHAT IF THE USER WANTS TO QUIT THIS CALCULATION AND START FRESH


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


def calculation():
  operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


  num1 = int(input("Whats the first number?\n"))


  should_continue = True
  while should_continue:

    num2 = int(input("Whats the next number?\n"))

    for key in operations:
      print(key)
    choose = input("pick a operation from the lines above.\n")
    calculation_funct = operations[choose]
    answer = calculation_funct(num1, num2)
    print(f"{num1} {choose} {num2} = {answer}")

    #if the user wants a frewsh start instead of using the previous calculation result./ 
    if (input(f"Type 'y' to continue or type 'n' to start a new function\n") == 'y'):
      num1 = answer
      
    else:
      calculation()



calculation()


############################################################################################################

import random

print("Welcome to the number Guessing Game!\n")
print("I am thinking of a number between 1 and 100\n")
difficulty = input("choose a difficulty.Type 'easy' or 'hard': \n")


def result(counter):
  myChoice = random.randint(0, 100)
  print(f"You have {counter} attepts remaining to guess the number")

  while counter > 0:
    userChoice = int(input("Make a guess: "))
    if (userChoice >= myChoice):
      print("Too high\n")
      print("Guess again!")
      print(f"You have {counter} attepts remaining to guess the number")
    elif (userChoice <= myChoice):
      print("Too low\n")
      print("Guess again!")
      print(f"You have {counter} attepts remaining to guess the number")
    else:
      print("You are Right!!!!")
    counter = counter - 1


if (difficulty == 'easy'):
  counter = 10
  result(counter)
elif (difficulty == 'easy'):
  counter = 5
  result(counter)
else:
  print("Wrong input")
  exit()

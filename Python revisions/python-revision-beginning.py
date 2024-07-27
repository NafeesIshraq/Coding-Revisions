# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random

random_toss = (random.random()) * 2 

if (random_toss < 1):
  print("Heads")
else:
  print ("Tails")

################
#EASIR WAY

random_toss2 = random.randint(0,1)

if random_toss2 == 1:
  print("Heads")
else:
  print ("Tails")
 
 
 
################ PYTHON LIST - DATA Structures

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

print(dirty_dozen[3]) # Accessing an item in a list by its index
print(dirty_dozen[-1]) # Accessing the last item in a list with negative 
#negetive indexes start backwards


#  extend insert remove pop append clear index count sort reverse copy -------- TRY IT

dirty_dozen.append("AngelaLand") #adds angelaland at the end of the list 

dirty_dozen.extend("","","") #can add  multiple items at once using extend
                        #it adds everything inside the brackets into the list
                        
                        
                        
#############

names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
size = len(names)
#size -1 because idex starts from 0 
random_name = random.randint(0,size-1)

print(f"{names[random_name]} is going to buy the meal today!")



############################ NESTED LIST 


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] #this is how two lists are nested/ we can nest as many as we want. 

print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])



#### name_of_the_main_list[index_number][index_number2]
#index_number = which list we want. choose the index of the list we want from the main list. 
#index_number2 = which element from the list i chose with first index number we want. 



print(dirty_dozen[0][1])  #this means. list in position 0, which is fruits. then show me the second element in that list (
print(dirty_dozen[1][2])  #this means list in the index 1, which is vegetables, then  element at index 2 which is tomatoes.

print(dirty_dozen[1][3])

#Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

#list = [['A', 'B, 'C'], 'E', 'F', 'G']
#E is list[1] C is list[0][2]


##########################################3

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
location = list(position)

Line_location = int(location[1])

row_number = Line_location -1
element_position = 0

if(location[0] == 'A'):
  element_position = 0
elif(location[0] == 'B'):
  element_position = 1
else:
  element_position =2

###### these if statements are not necessary 
#there is a function  for it called .index()
# variable_name = listname.index(value) # i want index 0 in list that contains all letters. #we will need a list too to store the letters.  
# value is whateven we want to check in that list. 



map[row_number][element_position] = "X"




# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")


#======================================================= Another menthod =================================================================

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")





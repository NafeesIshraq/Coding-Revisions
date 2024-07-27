print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
full_name = name1 + name2
#name1 = name1.lower()
#name2 = name2.lower()
#you are a fucking idot
#T1 = name1.count('t')
#T2 = name2.count('t')

lower_name = full_name.lower()


T = lower_name.count('t')
R = lower_name.count('r')
U = lower_name.count('u')
E = lower_name.count('e')

total1 = T+R+U+E


L = lower_name.count('l')
O = lower_name.count('o')
V = lower_name.count('v')
E = lower_name.count('e')

total2 = L+O+V+E

str_Love_score = str(total1)+str(total2)

Love_score = int(str_Love_score)


if Love_score <= 10 or Love_score >= 90:
  print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif Love_score>= 40 and Love_score <=50:
  print(f"Your score is {Love_score}, you are alright together.")
else:
  print(f"Your score is {Love_score}.")
  

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


highest_score = 0

#for n in range(0, len(student_scores)-1):
#  if(student_scores[n] > student_scores[n+1]):
 #   highest_score = student_scores[n]
 # else:
 #   highest_score = student_scores[n+1]


for n in range (0, len(student_scores)):
  if(student_scores[n] > highest_score):
    highest_score = student_scores[n]
print(f"The highest score in the class is: {highest_score}")



# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")




# Write your code here 👇
for n in range(1,101):
  if(n%5==0 and n%3==0):  #and operator first eh. weird bug. works jodi eita if statement hoi instead of elif
    print("FizzBuzz")
  elif(n%3==0):
    print("Fizz")
  elif(n%5==0):
    print("Buzz")
  else:
    print(n)
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {}
for key, value in student_scores.items():
  if value in range(91, 101):
    student_grades[key]="outstanding"
  elif value in range(81, 91):
    student_grades[key] = "Exceeds Expectations"
  elif value in range(71, 81):
    student_grades[key]= "Acceptable"
  else:
    student_grades[key] ="Fail"
    
    

    

# 🚨 Don't change the code below 👇
print(student_grades)






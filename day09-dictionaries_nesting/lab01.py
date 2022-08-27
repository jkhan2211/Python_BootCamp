student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        #print("Outstanding")
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 91:
        #print("Exceeds exception")
        student_grades[key] = "Exceeds exception"
    elif student_scores[key] >= 71 and student_scores[key] <= 81: 
        #print("Acceptable")
        student_grades[key] = "Acceptable"
    else:
        #print("Fail")
        student_grades[key] = "Fail"    

# 🚨 Don't change the code below 👇
print(student_grades)
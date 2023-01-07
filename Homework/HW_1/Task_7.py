# Write the code to check the student pass the class or not.
#To be able to pass the class student needs to have at least 65 
# score from the exams and student needs to attend the at least 
# 80 percent of all the classes. To calculate the average
# score we need to take take 20 percent of first exam score 
# and 30 percent of second exam score and 50 percent of thrd exam score. 
# We are going to use 3 varables for exam scores
# and one varable for attendance to classes.
# If condtions are met, pirnt True at the end. if not. print False.

first_exam = 70 * .20
second_exam = 80 * .30
third_exam = 85 * .50

avg_exam_score = (first_exam + second_exam + third_exam)

Attendence = 85

pass_class = (avg_exam_score >= 80.5) and (Attendence >= 80)
print("Student should pass the class", pass_class)

print
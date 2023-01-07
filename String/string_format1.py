
first_exam = 70 
second_exam = 90
third_exam = 78

# I want to create a string varible where I can display all grades of this students 

str = "First exam sscore is {}, second exam score is {}, third exam score is {}"

print(str.format(first_exam, second_exam, third_exam))
# First exam sscore is 70, second exam score is 90, third exam score is 78


str = "First exam sscore is {2}, second exam score is {1}, third exam score is {0}"

print(str.format(first_exam, second_exam, third_exam))
# First exam sscore is 78, second exam score is 90, third exam score is 70
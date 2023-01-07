# Ask user to enter a positive integer 
# Check if the given number is within 2 of a miltiple of 10.
# If it is within 2 of a multiple of 10 print,
#Your number is within 2 of multiple of 10
# If not print your number didnt match the expected requirement 

# 38 --> Your number is within 2 of multiple of 10 
# 52 --> Your number is within 2 of multiple of 10 
# 89 --> Your number is within 2 of multiple of 10 
# 7 --> Your number did not meet expected requirement 

# Which data type slicing belongs to? 
# String
# What would be the expected data type of given number? 
# int may be float

# 38 
# 38 // 10 -> 3 

# I need to use remainder with 10 
# 52 % 10 -> 2
# 51 % 10 -> 1
# 50 % 10 -> 0
# First condition to check for is if remainder with 10 giving less 
# than equals to 2.
# 89 % 10 -> 9
# 88 % 10 -> 8
# 38 % 10 -> 8
# OR second condition to check for is if the remainder with 10
# is bigger than equals to 8
print("ENter a number")
number = int(input())

first_condition = number % 10 <=2
second_condition = number % 10 >=8

result = first_condition or second_condition


if(result):
    print("Your number is within 2 of a multiple 10 ")
else:
    print("Your number didn't match the expected requirement.")














# Ask the user to enter one number between 1 to 10 then, Write the
# program to print the string in the following format:
# Search to see what happens when you multiply the string with
# numbers and use it for solving this question.
# Example: 
Input: 5 
# Output: 
# 1
# 22
# 333
# 4444
# 55555


for i in range (1,10):
  
    s = ""
    for x in range (1,i+1):
        s=s+" "+str(x)
    print(s)



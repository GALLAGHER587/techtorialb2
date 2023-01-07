
# Ask the user to give two different string values 
# If the first string contains the second string 
# print True, if not return false 

print(" Enter first text")
str1 = input() # good watch 

print ("Enter second text")
str2 = input () # good 


# If the string 1 doesnt contain the string 2 
# count of string 2 in string 1 should be 0
# If the count of string 2 in string 1 is not 0
# it means str1 contians  str2

is_contain = str1.count(str2)>0 


print(is_contain)






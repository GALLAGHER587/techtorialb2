
day = "Monday"
#      12345  6 will be the length of the string 
# .    012345 these are the index numbers in the string 

letter_4th = day [3]

print (letter_4th) # d

print(type(letter_4th)) # <class 'str'> 

# If the index number we are trying to access is biggeer than last index number
#  in the stirng it will throw index out of range error. 
#print(day[14])
 
# From the given string print out the last 2 letters?
print(day[4]+ day[5])
# What should i do to make my solutuion more dynamic?
# i need last two index from the string 
# last index in the string can be found by finding length of string and subtracting 1 
# day = "saturday"

last_index = len(day)-1 
second_to_last_index = last_index-1 

print(day[second_to_last_index] + day[last_index])

#when you use plus sign between 2 string values, it is called concatenation 

str1 = "Hello"
str2 = "World"
# Concatenate two strings above. 
print(str1 + str2)

print(len("text")) # 4
print("text"[2])   # x​

# len() you can always use with any string and find out lenght
# of the string. 
# Relation between length of the string and index numbers is 
# last index of the string is one smaller than length of the string. ​


 
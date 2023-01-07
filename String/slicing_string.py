# It will help us to get range of elements from the string 
# Syntax for using slicing 
#str[startingIndex: endIndex]

str = "saturday"
#      01234567  

print(str[2:5]) #tur 


# Create a progam to find middle three letters from given odd string
# "Chicago" --> ica 
# "seven"   --> eve

str = "seven" #seven 
# .    012345

last_index = len(str)-1 
middle_index = last_index // 2 

middle_three = str[middle_index-1:middle_index+2]

print(middle_three)















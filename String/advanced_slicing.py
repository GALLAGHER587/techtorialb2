
# 012345

s = "python"

print(s[-1]) # n

# index -1 will always be the last letter from the string 

print(s[-3]) # h

print (s[-4 : -1]) #tho 

print(s[-4 : -6]) # There is no letter in this scope 

print (s[3:1]) # There is no letter in this scope 


str1 = "Python is an object oriented"

print(str1[1:15:3])


# in slicing when there is 3 arguemnts 
# first one is starting index 
# second one is ending index
# third one is step 


# What do you think will happen when the step is negative 

city = "Chicago"

print(city[::-1]) # WILL REVERSE THE STRING 


# Ask user to enter any integer number and print that number reversed 

print("enter any integer number")

number = input()

print(number)

revered_num = number[::-1]

reverse_num = (revered_num)

print(revered_num)
print("Data type of this number is", type(revered_num))


# In 2 agrument slicing what happened?

s = "Techtorial"
print(s[4:2]) #Nothing 

# In 3 argument slicing when the step is negitive 

print(s[4:2:-1]) # th 

print(s[4:0:-2]) # tc





























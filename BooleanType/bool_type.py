
bool1 = True 
bool2 = False 

print(type(bool1)) # <class 'bool'>
print(type(bool2)) # <class 'bool'> 

print(bool1) # True
print(bool2) #False 

# We are trying to use arithmetucal operation using numerical value of the boolean varible 
#the Python makes sense of the expression below 
print(bool1 + 6) # 7

print(bool2 * 112) # 0 

# What happens when we use a comma between a number and a boolean varible 
print(bool2,6) # True 6
print(bool2,6) # False 6

# How to print string and boolean in single print function?
#Just use a comma between two varible 
print("the value of the bool1 is",bool1)
print("the value of the bool2 is",bool2)



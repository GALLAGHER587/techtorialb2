
# Ask user to enter a password
# The password should contain noth upper and lower case letters 
# If it contains both upper and lower case letter 
#print True, otherwise print false 


print("Enter your password")

password = input() # Techtorial 

# Varible lower is lower case version of the password 
lower = password.lower() # techtorial

# Varible upper is upper case version of the password 
upper = password.upper() # TECHTORIAL

# How can i understand if there is a lower case in this password
# I am going to create a boolean condition to check this 
# If this password is in all upper cases this password shouldbe equal to its upper case version 
# Therefore I can say if this password is not equal ot its upper case version it means it 
# contains some lower cases 


is_there_lower = password != upper 

is_there_upper = password != lower 

is_valid = is_there_lower and is_there_upper

print(is_valid)

























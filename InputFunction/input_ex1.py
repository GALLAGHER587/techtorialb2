
# Ask user to give you a string 
# Ask user to give order number of the letter and letter from the string 

print("Please enter any text ")
str = input()

print("""Please enter order number of the letter you want to see""")
order_num = int(input())



#user doesnt know index numbers in python
# The oreder number that user will give me will be one bigger than the index of the letter 

index_num = order_num - 1

print(str[index_num])














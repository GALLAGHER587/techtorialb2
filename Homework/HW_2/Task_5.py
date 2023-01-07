# Using an input function enter three different ingredients for the product
# on the same line. Then ask the user to enter any int number. Change the
# first letter of the ingredients starting from the entered number.
# (Ingredients should start with different letters. Please read the example carefully) 
# Example 1:
# Please enter three ingredients with spaces:
# Milk Peanuts Butter
# Please enter the int number:
# 5
# The output is:
# 5ilk 6eanuts 7utter

print("Enter three different ingredients")
ingredients = input()

print("enter any digit")
digit = int(input())

index_of_first_space = ingredients.find(" ")
first_word = ingredients[0:index_of_first_space]

last_index_of_space = ingredients.rfind(" ")
second_word = ingredients[index_of_first_space+1: last_index_of_space]

third_word = ingredients[last_index_of_space+1:]
 

# changing first letter of the first word
# remove the first lettr of the first word and add the number 
# at the beginning of the string 

first_word = str(digit)+first_word[1:]

digit += 1

second_word = str(digit) + second_word[1:]

digit += 1

third_word = str(digit) + third_word[1:]

print(first_word,second_word,third_word)





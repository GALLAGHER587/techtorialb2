# Ask the user to enter a random word using input function.
# Then ask the user to input the number of letters that word consists of.
# Lastly ask the user for a letter that they want to learn its index.
# Your code should print True if the user entered a right number of letters in the
# word. Print False if the wrong number is entered.
# Your code should print the index of the entered letter, if the word doesn’t
# contain the letter then the code should print -1.
# Please look at the example output below to understand how your code should work. 

# EXAMPLE OUTPUT:
# Enter a random word  
# Techtorial -> this line represents user's input
# Enter number of letter that word consists
# 10 -> this line represents user's input
# True
# Enter a letter that you want to find an index
# a -> this line represents user's input
# 8

print("Enter random word")
s1 = input()

print("Enter the number of letters in the string")
user_word = int(input())

print("Enter any letter")
letter = input()

is_user_word_correct = len(s1) == user_word
print(is_user_word_correct)

print(s1.find(letter))





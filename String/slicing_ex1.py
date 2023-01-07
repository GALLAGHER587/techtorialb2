
# Ask user to enter a string and print a rotated left 2 left versions. 
# Where the first 2 characters of the string moved to the end.

# "Hello" --> "lloHe"
# "java" -->   "vaja"


print(" please enter a word")
word = input()

# Using slicing we got first two letteers from the word 
first_two_letters = word [:2]

rest_of_string = word [2:]

rotated_word = rest_of_string + first_two_letters

print(rotated_word)






















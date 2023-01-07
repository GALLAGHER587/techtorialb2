# Reverse a given String and print it, if they have space in the
# beginning and at the end then remove it.  Without using
# slicing [ : :-1]. Try doing with for loop or while loop. 

# Example:  " Job" -> "boJ" 
# * " Happy " -> "yppaH" 
# * "Sun " -> "nuS" 
# * " Dream Job!" -> "!boJ maerD" 

print("Enter Text")

text = input()


length = len(text)
text_rev = ""
while length >0:
    text_rev += text[length -1]
    length = length-1 

print(text_rev)

#Ask user to enter any string value using input function.
#Then, remove all the spaces (" ") from the given string.
#After removing the spaces from the string,
#if the string's length is odd print True, otherwise print False.

# Example:
# Input: I love coding
# Output: True
# Input : one two
# Output: False
# "I love coding"
print ("enter string")
s = input ()

s = s. replace(" ","")

print (s)

string_length = (len (s))


if string_length % 2 != 0:
    print("True, string is odd")
else:
    print("False, string is even")

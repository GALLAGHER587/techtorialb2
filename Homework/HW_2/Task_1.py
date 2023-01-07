#Please use method chaining for the following Strings. Methods are
#provided next to the String.
#String “ Snicker " —> strip, upper, remove prefix and slice the string with
#any number of your choice
#String “Cookie” —> lower, replace ‘o’ with ‘u’, remove suffix e, 
# starts with ‘C’


s = "Snicker"
print(s.strip().upper().removeprefix("S")[2:5])






c = "Cookie"

print(c.lower().replace("o","u").removesuffix("e").startswith("C"))





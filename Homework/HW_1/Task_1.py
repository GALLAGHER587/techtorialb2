#Create a program that will add up the value of a number of
# quarters, dimes, nickels, and pennies. The number of each
#type of coin is input by the user. The total value is printed in dollars.
# Example:
Quarters: 5
Dimes: 4
Nickels: 3
Pennies: 2

# The total in dollars is $1.82
amount_of_q = 5
amount_of_d = 4
amount_of_n = 3
amount_of_p = 2
# Print amount of dollar this person has

value_of_q = 0.25
value_of_d = 0.10
value_of_n = 0.05
value_of_p = 0.01
amount_of_dollars = (amount_of_q * value_of_q) + (amount_of_d * value_of_d) + (amount_of_n * value_of_n) + (amount_of_p * value_of_p)
print (amount_of_dollars)
# Write a program that will take a given amount of money and return the number of dollars in quarters,
#dimes, nickels, and pennies that make up that given amount
#Example 1:
# Please enter your balance:
# 2.36
# $2.36 will make 9 quarters 1 dime 0 nickels and 1 pennies
#Example 2:
#Please enter your balance:
#5.22
# Output: $5.22 will make 20 quarters 2 dimes 0 nckels and 2 pennies
Balance = 2.36
# Convert change into cents
total_cents = 2.36 * 100

count_of_q = total_cents // 25

left_after_q = total_cents % 25

count_of_d = left_after_q // 10

left_after_d = left_after_q % 10

count_of_n = left_after_d // 5

count_of_p = left_after_d % 5

print ("For $", Balance, "I will return", count_of_q, "quaters", count_of_d, "dimes", count_of_n, "nickles", count_of_p, "pennies")
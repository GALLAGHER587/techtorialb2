#Write a program that wll accept 5 digit number and will print reversed number at the end.
#Example -1 :
# 53876
#The output is 67835
#Example-2:
# 97352
#The output is 25379

a = 53876
last_digit = a % 10

first_four_digigts= a // 10

fourth_digit = first_four_digigts % 10

first_three_digits = first_four_digigts // 10

third_digit = first_three_digits & 10

first_two_digits = first_three_digits // 10

second_digit = first_two_digits % 10

first_digit = first_two_digits // 10

print (last_digit, fourth_digit, third_digit, second_digit, first_digit)
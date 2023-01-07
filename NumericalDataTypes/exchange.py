# Create a python program to give 
# most efficient exchange possible using only 
# coins 
# quarter 25 cent
# nickel 5 cents
# dime is 10 cents
# penny 1 cent
# $2.34 exchange
# 9 quarters 
# 0 dimes 
# 1 nickel 
# 4 pennies
# $1.89
# 7 quarters 1 dimes and 0 nickels 4 pennies
# Create a program to give change using least coins possible. 
exchange = 1.89

#From the given amount of the exchange how many quaters can i use?

# I will convert exchange into cents 
total_cents = exchange * 100  



count_of_q = total_cents // 25 
print (count_of_q)
# i give enough quaters , however how can i complete the rest of the exchange? 
# I have to find what is left over after i give the qauters
# To find whats left over aftere giving the quater --->
left_after_quater = total_cents % 25 


# I have to find how many dimes I can give back 
count_of_dimes = left_after_quater // 10 

# I have to find what is left over afteer giving dimes 
left_after_dimes = left_after_quater % 10 

# I have to find how many nickle I can give 
count_of_nickle = left_after_dimes // 5 

count_of_pennies = left_after_dimes % 5 

print("For $", exchange, "I will give", count_of_q,"quaters"
, count_of_dimes, "dimes", count_of_nickle, "nickles", count_of_pennies, "pennies")







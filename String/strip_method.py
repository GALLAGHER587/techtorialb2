
# We can ask user to enter a string and remove the spaces in the beginning and at the end of the string 

str = "     Techtorial           "

print(str)
print(str.strip())


# In strip method we can provide a character and it will remove that character 
# from the beggining and end of the string 


# Lets write a phone number in the middle of ### hashtags 

phone_num = "###8475020677###"

print(phone_num.strip('#'))



# We can use strip method with multiple characters as well 

web_site = "www.techtorialacadamy.com"
# I want to get the domain name 

print(" Domain name of this website is", web_site.strip("o.wmc"))

















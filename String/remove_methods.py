
# remove suffix --> will remove it from the end of the string 
# remove prefix will remove it from beggingin of the string 

s = "Hello World"

print(s.removeprefix("World")) # Hello World 

print(s.removeprefix("Hello")) #   World 

print(s.removesuffix("World")) # Hello 

print(s.removeprefix("olleH")) # Hello World 

# Unlike the strip method, in remove suffix and prefix method 
# oreder of the characters are important 

print(s.strip("elloH")) # World 


print(s.removeprefix("He")) # llo World 
print(s.removesuffix("ld")) # Hello Wor


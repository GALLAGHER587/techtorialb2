txtlen = 0 # if txtlen remains 0 keep prompting the user to enter something
while txtlen == 0:
    print('Please enter your name')
    txt = input().replace(' ','') # replace is chained on input()
    txtlen = len(txt) # if the user doesn't enter anything or just blank spaces the while loop will keep running

print(txt)
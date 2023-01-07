#Using input function ask user to enter a song name. 
# 1. Print the first charachter of given song name.
# 2. Print the last charachter of given song name.
# 3. Print the length of the given song name.
# 4. Print the index number of "k" in this song name. 
# 5. Print the charachter from an index number of 3. 
# 6. Print the song name in upper case.
# 7. Print the song name in lower case.

print("enter song name")
song_name = input()
 
# first_char = song_name [0]
print(song_name[0])


# last_char = song_name [-1]
print(song_name[-1])

#length = len(song_name) 
print (len(song_name))

print(song_name.find("k"))


# char_k = song_name [3]
print(song_name[3])

print(song_name.upper())

print(song_name.lower())

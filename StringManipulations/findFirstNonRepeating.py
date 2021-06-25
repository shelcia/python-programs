# Given a string, find the first non-repeating
# character in it and return its index. If it doesn't exist, return -1.

# string = str(input(''))
string = 'shelcia'
frequencies = {}
index = 0

for char in string:
    if(index):
        if(frequencies[string[index-1]] == 1):
            print(string[index-1])
            break
    if(char in frequencies):
        frequencies[char] += 1
    else:
        frequencies[char] = 1

    index = index + 1

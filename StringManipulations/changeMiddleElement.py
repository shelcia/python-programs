# Given a string S, print it after changing the middle element to *
# (if the length of the string is even, change the 2 middle elements to *).
string = str(input(""))
array = list(string)

if(len(array) % 2 == 0):
    array[len(array)//2] = '*'
    array[len(array)//2 - 1] = '*'
else:
    array[len(array)//2] = '*'

for index in range(0, len(array)):
    print(array[index], end="")

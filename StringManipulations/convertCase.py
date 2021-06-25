# Write a program to get a string S, Type of conversion (1 - Convert to Lowercase,
# 2 - Convert to Uppercase) T, and integer P . Convert the case of the letters in the
# positions which are multiples of P.(1 based indexing).

# Sample Input :
# ProFiLe
# 1
# 2
# Sample Output :
# Profile


string = str(input(''))
type = int(input(''))
multiple = int(input(''))


array = list(string)
newArray = []

for index in range(0, len(array)):
    if((index+1) % multiple == 0):
        if(type == 1):
            newArray.append(array[index].lower())
        else:
            newArray.append(array[index].upper())
    else:
        newArray.append(array[index])

for index in range(0, len(newArray)):
    print(newArray[index], end='')

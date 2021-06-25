# Radha newly learnt about palindromic strings.A palindromic string is a string
# which is same when read from left to right and also from right to left.
# Help her in implementing the logic.

string = str(input(''))
array = list(string)
revArray = array
revArray.reverse()
# print('rev: ',revArray)
N = len(array)

count = 0

for index in range(0, N):
    if(str(array[index]) != str(revArray[N-index-1])):
        count = count+1

if(count == 0):
    print(1)
else:
    print(0)

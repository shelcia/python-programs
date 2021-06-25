# Rahul is given a task to manipulate a string, He hired you as a
# developer your task is to delete all the repeating characters and print the result left.

string = str(input(''))
array = list(string)
ignoredIndex = []
newArray = []
N = len(array)

for index in range(0, N):
    for alphaIndex in range(index+1, N):
        if(array[index] == array[alphaIndex]):
            ignoredIndex.append(alphaIndex)
            ignoredIndex.append(index)

for index in range(0, N):
    if(not(index in ignoredIndex)):
        newArray.append(array[index])

for index in range(0, len(newArray)):
    print(newArray[index], end='')

# FINDING SMALLEST AND LARGEST INDEXES
# N = int(input(""))
# Array = list(map(int, input().split(' ')[:N]))
Array = [32, 14, 12, 98, 24, 56, 76, 34]
max = Array[0]
min = Array[0]
maxIndex = 0
minIndex = 0
for i in range(1, len(Array)):
    if(max < Array[i]):
        max = Array[i]
        maxIndex = i
    elif(min > Array[i]):
        min = Array[i]
        minIndex = i
print("Index", minIndex+1, maxIndex+1)
print(min, max)

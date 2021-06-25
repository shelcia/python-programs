# Given a number N and a list of N elements, find the length of the longest repeating sequence of the elements. If no such sequence is found print -1
# Input Size : N <= 100000


N = int(input(''))
array = list(map(int, input().split(' ')[:N]))
maxRepeat = 1
array.sort()
index = 0

while index < N:
    count = 0
    for j in range(index, N):
        if(array[index] == array[j]):
            count = count+1
            if(maxRepeat < count):
                maxRepeat = count
        else:
            index = index+j
            break

if(maxRepeat == 1):
    print(-1)
else:
    print(maxRepeat)

# 1 2 2 2 3 4 5

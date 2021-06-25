# Find the repeating and the missing

# Given an unsorted array of size n. Array elements are in the range from 1 to n.
# One number from set {1, 2, …n} is missing and one number occurs twice in the array.
# Find these two numbers.


def repeatingMissing(arr):
    # O(nlogn)-> Time Complexity O(1)-> Space Complexity
    arr.sort()
    flag = 1
    for i in range(len(arr)):
        if(flag == arr[i]):
            flag += 1
        elif(arr[i] == arr[i-1]):
            print('repeating number', arr[i])
    print('mising number', flag)

    # O(n)-> Time Complexity O(n)-> Space Complexity
    hashmap = []
    print('repeating number', '')
    for i in range(len(arr)):
        if(arr[i] in hashmap):
            print(arr[i], '')
        else:
            hashmap.append(arr[i])

    for i in range(1, len(arr)+1):
        if (i not in arr):
            print('mising number', i)


if __name__ == '__main__':
    arr = [7, 3, 4, 5, 5, 6, 2]
    arr2 = [4, 3, 6, 2, 1, 1]
    repeatingMissing(arr)
    repeatingMissing(arr2)

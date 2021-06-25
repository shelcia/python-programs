# Given an array of n elements that contains elements from 0 to n-1,
# with any of these numbers appearing any number of times.
# Find these repeating numbers in O(n) and using only constant memory space.


def duplicateArray(arr):

    # Approach 1 - we will create hash map

    # hashmap = []

    # for i in range(len(arr)):
    #     if(arr[i] in hashmap):
    #         print(arr[i])
    #     else:
    #         hashmap.append(arr[i])

    # Approach 2 - O(1) space complexity O(n) time complexity
    # If I have same two number its reminder when divided by array size
    # would be same which means I will be increementing the very same array element twice

    print('length', len(arr), 'arr', arr)
    for i in range(len(arr)):

        x = arr[i] % len(arr)
        arr[x] = arr[x] + len(arr)
        print('x:', x, 'arr[x]:', arr[x], 'array', arr)

    print("The repeating elements are : ")
    for i in range(len(arr)):
        if (arr[i] >= len(arr)*2):
            print(i, " ")


if __name__ == '__main__':
    arr = [1, 2, 3, 6, 3, 6, 1]
    duplicateArray(arr)

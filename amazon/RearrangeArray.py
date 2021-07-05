# Rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space

# Given an array arr[] of size n where every element is in range from 0 to n-1.
# Rearrange the given array so that arr[i] becomes arr[arr[i]].
# This should be done with O(1) extra space.

# Examples:

# Input: arr[]  = {3, 2, 0, 1}
# Output: arr[] = {1, 0, 3, 2}
# Explanation:
# In the given array
# arr[arr[0]] is 1 so arr[0] in output array is 1
# arr[arr[1]] is 0 so arr[1] in output array is 0
# arr[arr[2]] is 3 so arr[2] in output array is 3
# arr[arr[3]] is 2 so arr[3] in output array is 2

# Input: arr[] = {4, 0, 2, 1, 3}
# Output: arr[] = {3, 4, 2, 0, 1}
# Explanation:
# arr[arr[0]] is 3 so arr[0] in output array is 3
# arr[arr[1]] is 4 so arr[1] in output array is 4
# arr[arr[2]] is 2 so arr[2] in output array is 2
# arr[arr[3]] is 0 so arr[3] in output array is 0
# arr[arr[4]] is 1 so arr[4] in output array is 1

# Input: arr[] = {0, 1, 2, 3}
# Output: arr[] = {0, 1, 2, 3}
# Explanation:
# arr[arr[0]] is 0 so arr[0] in output array is 0
# arr[arr[1]] is 1 so arr[1] in output array is 1
# arr[arr[2]] is 2 so arr[2] in output array is 2
# arr[arr[3]] is 3 so arr[3] in output array is 3


def rearrangeArray(arr, n):

    # First step: Increase all values
    # by (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
        print(i, ':', arr)

    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)
        print(i, ':', arr)


def printArr(arr, n):

    for i in range(0, n):
        print(arr[i], end=" ")
    print("")


if __name__ == "__main__":
    arr = [3, 2, 0, 1]
    n = len(arr)

    print("Given array is")
    printArr(arr, n)

    rearrangeArray(arr, n)
    print("Modified array is")
    printArr(arr, n)

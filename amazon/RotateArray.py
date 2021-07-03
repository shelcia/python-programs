# Program for array rotation


# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# 1) Store the first d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]

# 0 -> n-1-k+i

def rotateLeftArray(arr, k):
    n = len(arr)
    if k > n:
        k = k % n

    temp = arr[:k]
    for i in range(k, n):
        arr[i-k] = arr[i]
    arr = arr[:n-k]
    arr = arr + temp
    print(arr)


def rotateRightArray(arr, k):
    n = len(arr)
    if k > n:
        k = k % n

    temp = arr[k+1:]
    print(temp + arr[:n-k])


# rotateLeftArray([1, 2, 3, 4, 5, 6, 7], 2)  # [3, 4, 5, 6, 7, 1, 2]

rotateRightArray([1, 2, 3, 4, 5, 6, 7], 3)  # [5,6,7,1,2,3,4]

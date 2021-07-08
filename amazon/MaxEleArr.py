# Find the maximum element in an array which is first increasing and then decreasing

# Given an array of integers which is initially increasing and then decreasing,
# find the maximum value in the array.
# Examples :


# Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
# Output: 500

# Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
# Output: 50

# Corner case (No decreasing part)
# Input: arr[] = {10, 20, 30, 40, 50}
# Output: 50

# Corner case (No increasing part)
# Input: arr[] = {120, 100, 80, 20, 0}
# Output: 120


# BINARY SEARCH

# Time complexity -> O(logn)
# Space complexity -> O(1)

def findMax(arr, high, low):

    # base cases

    if high == low:
        return arr[high]

    if high == low + 1 and arr[high] >= arr[low]:
        return arr[high]

    if high == low + 1 and arr[high] <= arr[low]:
        return arr[low]

    # otherwise
    mid = (high+low)//2

    # if mid element is the max
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return arr[mid]

    # If arr[mid] is greater than the next element and smaller than the previous
    # element then maximum lies on left side of mid
    if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
        return findMax(arr, mid - 1, low)
    # when arr[mid] is greater than arr[mid-1] and smaller than arr[mid+1]
    else:
        return findMax(arr, high, mid + 1)


arr = [120, 100, 80, 20, 0]
print(findMax(arr, len(arr), 0))

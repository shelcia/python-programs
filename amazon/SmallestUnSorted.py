# Find the smallest positive number missing from an unsorted array

# You are given an unsorted array with both positive and negative elements.
# You have to find the smallest positive number missing from the array in O(n) time using
# constant extra space. You can modify the original array.

# Examples

#  Input:  {2, 3, 7, 6, 8, -1, -10, 15}
#  Output: 1

#  Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
#  Output: 4

#  Input: {1, 1, 0, -1, -2}
#  Output: 2


def findSmallest(nums):

    nums.sort()

    for num in range(1, nums[len(nums)-1]+1000):
        if(num not in nums):
            return num


print(findSmallest([2, 3, 7, 6, 8, -1, -10, 15]))
print(findSmallest([2, 3, -7, 6, 8, 1, -10, 15]))
print(findSmallest([1, 1, 0, -1, -2]))

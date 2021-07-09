# Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and
# ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

def binarySearch(nums, target, leftBias):

    l, r = 0, len(nums) - 1
    idx = -1

    while l <= r:

        m = (l+r)//2

        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            idx = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return idx


def searchRange(nums, target):

    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)

    return [left, right]


print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([], 0))

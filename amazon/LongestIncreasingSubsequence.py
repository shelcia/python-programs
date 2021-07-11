# Longest Increasing Subsequence


# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or
# no elements without changing the order of the remaining elements. For example, [3,6,2,7]
# is a subsequence of the array [0,3,1,6,2,2,7].


# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104


# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


# def lengthOfLIS(nums):

#     n = len(nums)
#     LIS = [1] * n

#     for i in range(n-1, -1, -1):
#         for j in range(i+1, n):
#             if nums[i] < nums[j]:
#                 LIS[i] = max(LIS[i], 1 + LIS[j])
#     print(max(LIS))

from bisect import bisect_left


def lengthOfLIS(nums):
    dp = []
    for i in range(len(nums)):
        pos = bisect_left(dp, nums[i])
        if pos == len(dp):
            dp.append(nums[i])
        else:
            dp[pos] = nums[i]
    print(len(dp))


lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
lengthOfLIS([0, 1, 0, 3, 2, 3])
lengthOfLIS([7, 7, 7, 7, 7, 7, 7])

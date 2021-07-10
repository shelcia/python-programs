# Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive
# elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


class Solution:
    def longestConsecutive(self, nums):

        hashmap = set(nums)

        maxLength = 0


#         iterate thrugh all elements and check if any of them
#         have right consecutive number

#         form list only if the element doesn't have left nieghbour
#         i.e for 4 left neughboar is 3  (numerically)

        for num in nums:
            if num - 1 not in hashmap:
                curLength = 0
                while num + curLength in hashmap:
                    curLength += 1

                maxLength = max(maxLength, curLength)

        return maxLength

# i/ps:

# [100,4,200,1,3,2]
# [0,3,7,2,5,8,4,6,0,1]
# []
# [-2, -4, -5, 6, -3, 8]

# o/p:
# 4
# 9
# 0
# 4

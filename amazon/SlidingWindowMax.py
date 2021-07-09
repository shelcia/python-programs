# Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which
# is moving from the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Example 3:

# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:

# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:

# Input: nums = [4,-2], k = 2
# Output: [4]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


# Time Complexity -> O(n)

import collections


def SlidingWindowMax(nums, k):
    res = []

    # l is the pointed towards forst element in the window and would be reassigned
    # if we out of bound of the window

    # r keep moving across all elements in th window
    l, r = 0, 0

    queue = collections.deque()

    # monotonically decresing queue

    while r < len(nums):

        # element is queue are just indexes
        # pop until we are within the window and the next element is greater than pre existing
        # queue values thus we make sure when we pop the queue we get the max ele in window

        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()

        # add the index in the queue
        queue.append(r)

        # remove left val from window if it is no longer in bound
        if l > queue[0]:
            queue.popleft()

        # window crossing the bound
        if r - l >= k - 1:
            # add the max element
            res.append(nums[queue[0]])
            l += 1

        # loop incrementation
        r += 1
    return res


print(SlidingWindowMax([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(SlidingWindowMax([1], 1))
print(SlidingWindowMax([1, -1], 1))
print(SlidingWindowMax([9, 11], 2))
print(SlidingWindowMax([4, -2], 2))

# o/p
# [3,3,5,5,6,7]
# [1]
# [1,-1]
# [11]
# [4]

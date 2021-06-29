
# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# We will be using memoization

def uniquePaths(m, n, memo={}):

    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]

    # Base cases
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = uniquePaths(m-1, n, memo) + uniquePaths(m, n-1, memo)
    return memo[key]


print(uniquePaths(3, 7))

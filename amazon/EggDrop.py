# Super Egg Drop


# You are given k identical eggs and you have access to a building with n floors labeled
# from 1 to n.

# You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a
# floor higher than f will break, and any egg dropped at or below floor f will not break.

# Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n).
# If the egg breaks, you can no longer use it. However, if the egg does not break,
# you may reuse it in future moves.

# Return the minimum number of moves that you need to determine with certainty what
# the value of f is.

# Example 1:

# Input: k = 1, n = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1. If it breaks, we know that f = 0.
# Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
# If it does not break, then we know f = 2.
# Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
# Example 2:

# Input: k = 2, n = 6
# Output: 3
# Example 3:

# Input: k = 3, n = 14
# Output: 4


# Constraints:

# 1 <= k <= 100
# 1 <= n <= 104

def superEggDrop(K, N):

    # Right now, dp[i] represents dp(1, i)
    dp = range(N+1)

    for k in range(2, K+1):
        # Now, we will develop dp2[i] = dp(k, i)
        dp2 = [0]
        x = 1
        for n in range(1, N+1):
            # Let's find dp2[n] = dp(k, n)
            # Increase our optimal x while we can make our answer better.
            # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
            # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
            while x < n and max(dp[x-1], dp2[n-x]) > \
                    max(dp[x], dp2[n-x-1]):
                x += 1

            # The final answer happens at this x.
            dp2.append(1 + max(dp[x-1], dp2[n-x]))

        dp = dp2

    return dp[-1]

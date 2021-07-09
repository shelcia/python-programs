# Count ways to reach the n’th stair

# There are n stairs, a person standing at the bottom wants to reach the top.
# The person can climb either 1 stair or 2 stairs at a time. Count the number of ways,
# the person can reach the top.

# Examples:

# Input: n = 1
# Output: 1
# There is only one way to climb 1 stair

# Input: n = 2
# Output: 2
# There are two ways: (1, 1) and (2)

# Input: n = 4
# Output: 5
# (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)


# memoization
def CountStepsI(n, memo={}):

    if n in memo:
        return memo[n]

    # Base cases
    if n == 1 or n == 0:
        return 1

    memo[n] = CountStepsI(n-1, memo) + CountStepsI(n-2, memo)
    return memo[n]

# botto up approach


def CountStepsII(steps):

    one, two = 1, 1

    while steps != 0:

        temp = one
        one = one + two
        two = temp

        # print(one, two)
        steps -= 1

    return two


steps = 4

print(CountStepsI(steps))
print(CountStepsII(steps))


# def climbStairs(n):

# 	# helper
# 	def recurse(n):
# 		if n == 0 or n == 1:
# 			return 1

# 		return recurse(n-1) + recurse(n-2)

# 	# main
# 	return recurse(n)

# 2. Top-down recursive | With memoization

# def climbStairs(n):

# 	# helper
# 	def recurse(n):
# 		if n == 0 or n == 1:
# 			return 1

# 		if n in d:
# 			return d[n]
# 		d[n] = recurse(n-1) + recurse(n-2)
# 		return d[n]

# 	# main
# 	d = {}
# 	return recurse(n)
# 3. Bottom-up itertaive with tabulization

# def climbStairs(n):

# 	table = [0]*(n+1) # this stores how many ways to arrive at each index/step - NOTE [1]

# 	table[0] = 1 # only one way to arrive at index 0 (this is basically the starting point aka ground level)
# 	table[1] = 1 # only one way to arrive at index 1 (first step)

# 	# for remaining steps/indicies, each can be arrived at from: a) 1 step away, b) 2 steps away
# 	for i in range(2, len(table)):
# 		table[i] = table[i-1] + table[i-2]

# 	return table[n]

# # NOTE [1]
# # Use (n+1) so that we can have index 0 for when person is at the ground level still

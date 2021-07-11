# Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8

def generateParenthesis(n):

    stack = []
    res = []

    def backtrack(openCt, closeCt):
        print(stack)

        if openCt == closeCt == n:
            res.append("".join(stack))
            return

        if openCt < n:
            stack.append("(")
            backtrack(openCt+1, closeCt)
            stack.pop()

        if closeCt < openCt:
            stack.append(")")
            backtrack(openCt, closeCt + 1)
            # clean stack
            stack.pop()

    backtrack(0, 0)
    print(res)


generateParenthesis(3)

# Print all combinations of balanced parentheses

# Write a function to generate all possible n pairs of balanced parentheses.

# Examples:

# Input: n=1
# Output: {}
# Explantaion: This the only sequence of balanced
# parenthesis formed using 1 pair of balanced parenthesis.

# Input : n=2
# Output:
# {}{}
# {{}}
# Explantaion: This the only two sequences of balanced
# parenthesis formed using 2 pair of balanced parenthesis.


def printParanthesis(n):

    str = [""]*2*n
    _printParanthesis(str, n, 0, 0, 0)


def _printParanthesis(str, n, pos, open, close):

    if close == n:
        for i in str:
            print(i, end="")
        print()
        return

    else:
        if (open > close):
            str[pos] = "}"
            _printParanthesis(str, n, pos+1, open, close + 1)

        if (open < n):
            str[pos] = "{"
            _printParanthesis(str, n, pos+1, open + 1, close)


printParanthesis(3)

# Python3 program to
# Print all combinations
# of balanced parentheses

# Wrapper over _printParenthesis()
def printParenthesis(str, n):
    if(n > 0):
        _printParenthesis(str, 0,
                          n, 0, 0)
    return


def _printParenthesis(str, pos, n,
                      open, close):

  # print('str', str)

    if(close == n):
        for i in str:
            print('paran', i, end="")
        print()
        return
    else:
        # print('str', str)
        if(open > close):
            str[pos] = '}'
            _printParenthesis(str, pos + 1, n,
                              open, close + 1)
        if(open < n):
            str[pos] = '{'
            _printParenthesis(str, pos + 1, n,
                              open + 1, close)


# Driver Code
n = 3
str = [""] * 2 * n
printParenthesis(str, n)

# This Code is contributed
# by mits.

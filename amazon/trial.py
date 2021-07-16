# Python3 program to
# Print all combinations
# of balanced parentheses

# Wrapper over _printParenthesis()
# def printParenthesis(str, n):
#     if(n > 0):
#         _printParenthesis(str, 0,
#                           n, 0, 0)
#     return


# def _printParenthesis(str, pos, n,
#                       open, close):

#   # print('str', str)

#     if(close == n):
#         for i in str:
#             print('paran', i, end="")
#         print()
#         return
#     else:
#         # print('str', str)
#         if(open > close):
#             str[pos] = '}'
#             _printParenthesis(str, pos + 1, n,
#                               open, close + 1)
#         if(open < n):
#             str[pos] = '{'
#             _printParenthesis(str, pos + 1, n,
#                               open + 1, close)


# # Driver Code
# n = 3
# str = [""] * 2 * n
# printParenthesis(str, n)

class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    # Base Case
    if root is None:
        return None

    # if one of the them is the ancestor itself
    if root == p or root == q:
        return root.val

    # look for keys in subtree
    leftTree = lowestCommonAncestor(root.left, p, q)
    rightTree = lowestCommonAncestor(root.right, p, q)

    # if subtrees return non null then ancestor is the root of these two subtree
    if leftTree and rightTree:
        return root.val

    # reducing our tree
    return leftTree if leftTree is not None else rightTree


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("LCA(4, 5) = %d" % (lowestCommonAncestor(
        root, root.left.left, root.left.right,)))
    print("LCA(4, 6) = %d" % (lowestCommonAncestor(
        root, root.left.left, root.right.left)))
    print("LCA(3, 4) = %d" %
          (lowestCommonAncestor(root, root.right, root.left.left)))
    print("LCA(2, 4) = %d" %
          (lowestCommonAncestor(root, root.left, root.left.left)))

    print("LCA(4, 5) = %d" % (lowestCommonAncestor(
        root, root.left.left, root.left.right,)))

# Maximum Path Sum in a Binary Tree


# Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.
# Example:

# Input: Root of below tree
#        1
#       / \
#      2   3
# Output: 6

# See below diagram for another example.
# 1+2+3

# 1. Node only
# 2. Max path through Left Child + Node
# 3. Max path through Right Child + Node
# 4. Max path through Left Child + Node + Max path through Right Child
# The idea is to keep trace of four paths and pick up the max one in the end.
# An important thing to note is, root of every subtree need to return maximum path
# sum such that at most one child of root is involved. This is needed for parent function call.


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorderTraversal(node):

    # Base Case
    if node is None:
        return 0

    l = max(postorderTraversal(node.left), 0)
    r = max(postorderTraversal(node.right), 0)

    # WITH SPLIT HAPPENING IN ROOT
    postorderTraversal.res = max(postorderTraversal.res, node.data + l + r)

    # WITHOUT SPLIT HAPPENING IN ROOT
    return node.data + max(l, r)


def findMaxSum(root):

    postorderTraversal.res = float("-inf")

    if root is not None:
        postorderTraversal(root)

    return postorderTraversal.res


root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print("Max path sum is ", findMaxSum(root))


#              10
#            /   \
#          2      10
#        /  \      \
#      20    1     25
#                /   \
#               3     4

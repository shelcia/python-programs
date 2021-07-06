# Find Minimum Depth of a Binary Tree

# Given a binary tree, find its minimum depth. The minimum depth is the number of nodes
# along the shortest path from the root node down to the nearest leaf node.

# For example, minimum height of below Binary Tree is 2.

# Note that the path must end on a leaf node. For example, the minimum height of below
# Binary Tree is also 2.

#           10
#         /
#       5

# The idea is to traverse the given Binary Tree. For every node, check if it is a leaf node.
# If yes, then return 1. If not leaf node then if the left subtree is NULL, then recur for
# the right subtree. And if the right subtree is NULL, then recur for the left subtree.
# If both left and right subtrees are not NULL, then take the minimum of two heights.


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def minDepth(root):

    if root is None:
        return 0

    queue = [root]
    level = []

    res = 1

    while queue != []:

        for node in queue:

            if node.left is None and node.right is None:
                return res
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)

        queue = level
        level = []
        res += 1

    return res


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(minDepth(root))

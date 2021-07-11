# Kth Smallest Element in a BST


# Given the root of a binary search tree, and an integer k, return the kth (1-indexed)
# smallest element in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
# and you need to find the kth smallest frequently, how would you optimize?

class Node:

    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderTrvaersal(node):
    if node is None:
        return []

    return inorderTrvaersal(node.left) + [node.val] + inorderTrvaersal(node.right)


def kthSmallest(root, k):

    arr = inorderTrvaersal(root)

    print(arr[k-1])


root = Node(3)
root.left = Node(1)
root.right = Node(4)
root.left.right = Node(1)

kthSmallest(root, 1)
# Output: 1

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)

kthSmallest(root, 3)
# Output: 3

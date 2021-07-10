# ZigZag Tree Traversal


# Write a function to print ZigZag order traversal of a binary tree.
# For the below binary tree the zigzag order traversal will be 1 3 2 7 6 5 4.

# Given the root of a binary tree, return the zigzag level order traversal of its
# nodes' values. (i.e., from left to right, then right to left for the next level and
# alternate between).


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):

        if root is None:
            return []

        queue = [root]
        level = []
        res = [[root.val]]
        isReversed = True

        while queue != []:
            tempLevelValues = []

            for node in queue:
                if node.left:
                    level.append(node.left)
                    tempLevelValues.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    tempLevelValues.append(node.right.val)

            if level == []:
                break

            if isReversed:
                tempLevelValues = tempLevelValues[::-1]
                res.append(tempLevelValues)
            else:
                res.append(tempLevelValues)

            queue = level
            level = []
            isReversed = not isReversed

        print(res)
        return res

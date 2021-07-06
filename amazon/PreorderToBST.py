# Construct BST from given preorder traversal

# Given preorder traversal of a binary search tree, construct the BST.

# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be
# the root of the following tree.

#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50


# A O(n) program for construction of BST from preorder traversal

INT_MIN = float("-infinity")
INT_MAX = float("infinity")

# A Binary tree node


class Node:

    # Constructor to created a new node
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Methods to get and set the value of static variable
# constructTreeUtil.preIndex for function construcTreeUtil()


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def _insertNode(self, node, value):

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insertNode(node.left, value)

        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insertNode(node.right, value)

    def insertNode(self, value):

        node = Node(value)

        if(self.root is None):
            self.root = node
        else:
            self._insertNode(self.root, value)

    def _inorderTraversal(self, currentNode):
        if currentNode is None:
            return []

        return (self._inorderTraversal(currentNode.left) +
                [currentNode.value] + self._inorderTraversal(currentNode.right))

    def inorderTraversal(self):
        if self.root is None:
            return []

        return self._inorderTraversal(self.root)


if __name__ == "__main__":

    instance = BinaryTree()

    print('print')
    print(instance.inorderTraversal())

    # instance.constructTree([10, 5, 1, 7, 40, 50])

    preorder = [10, 5, 1, 7, 40, 50]

    for i in range(len(preorder)):
        instance.insertNode(preorder[i])

    print('print')
    print(instance.inorderTraversal())

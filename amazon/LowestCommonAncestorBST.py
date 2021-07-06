# Lowest Common Ancestor in a Binary Tree | Set 1

# Given a binary tree (not a binary search tree) and two values say n1 and n2,
# write a program to find the least common ancestor.

# Following is definition of LCA from Wikipedia:
# Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is
# defined as the lowest node in T that has both n1 and n2 as descendants
# (where we allow a node to be a descendant of itself).
# The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from
# the root. Computation of lowest common ancestors may be useful, for instance, as part of a
# procedure for determining the distance between pairs of nodes in a tree: the distance from
# n1 to n2 can be computed as the distance from the root to n1, plus the distance from the root
# to n2, minus twice the distance from the root to their lowest common ancestor. (Source Wiki)

class binaryTreeNode:

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right


class binaryTree:

    # To store paths to n1 and n2 fromthe root

    def __init__(self, root=None):
        self.root = root
        self.path1 = []
        self.path2 = []

    def _findLCARec(self, root, node1, node2):

        # Current Pointer
        cur = root

        while cur:
            print('current value', cur.value, node1, node2)

            if int(cur.value) < node1 and int(cur.value) < node2:
                cur = cur.right
            elif int(cur.value) > node1 and int(cur.value) > node2:
                cur = cur.left
            else:
                return cur.value

    def findLCARec(self, node1, node2):
        if self.root is None:
            return 0
        print(self.root.value, node1, node2)
        return self._findLCARec(self.root, node1, node2)

    def _insertNode(self, node, value):

        if value < node.value:
            if node.left is None:
                node.left = binaryTreeNode(value)
            else:
                self._insertNode(node.left, value)

        elif value > node.value:
            if node.right is None:
                node.right = binaryTreeNode(value)
            else:
                self._insertNode(node.right, value)

    def insertNode(self, value):

        node = binaryTreeNode(value)

        if(self.root is None):
            self.root = node
        else:
            self._insertNode(self.root, value)

    def inorderTraversal(self, currentNode):

        if(currentNode is None):
            return []

        return self.inorderTraversal(currentNode.left) + [currentNode.value] + self.inorderTraversal(currentNode.right)

    def printBinaryTree(self):

        return self.inorderTraversal(self.root)


if __name__ == "__main__":

    nodeInstance = binaryTree()

    nodeInstance.insertNode('5')
    nodeInstance.insertNode('4')
    nodeInstance.insertNode('6')
    nodeInstance.insertNode('3')
    nodeInstance.insertNode('9')
    nodeInstance.insertNode('2')
    nodeInstance.insertNode('1')
    nodeInstance.insertNode('7')
    nodeInstance.insertNode('11')

    print('inorder', nodeInstance.printBinaryTree())
    print('findrec', nodeInstance.findLCARec(7, 11))

#             5
#           /  \
#         4     6
#        /       \
#       3         9
#      /         / \
#     2         7   11
#    /
#   1

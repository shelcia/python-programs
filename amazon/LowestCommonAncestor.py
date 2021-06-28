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

    def __init__(self, root=None):
        self.root = root

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

    def _findPath(self, node, key, path):

        if node is None:
            return False

        path.append(node.value)

        if node.value == key:
            return True

        if ((node.left != None and self._findPath(node.left, key, path)) or
                (node.right != None and self._findPath(node.right, key, path))):
            return True

        if(len(path)):
            path.pop()
        return False

    def findPath(self, key, path):
        if self.root is None:
            return False

        path.append(self.root.value)

        print(self.root.value, key)
        if(self.root.value == key):
            return True

        else:
            self._findPath(self.root, key, path)

    def LCA(self, node1, node2):

        path1 = []
        path2 = []

        if(self.findPath(node1, path1) and self.findPath(node2, path2)):
            return -1

        i = 0
        while (i < len(path1) and i < len(path2)):
            if (path1[i] != path2[i]):
                break
            i += 1

        return path1


if __name__ == "__main__":

    nodeInstance = binaryTree()

    nodeInstance.insertNode('5')
    nodeInstance.insertNode('4')
    nodeInstance.insertNode('6')
    nodeInstance.insertNode('3')
    nodeInstance.insertNode('7')
    nodeInstance.insertNode('2')
    nodeInstance.insertNode('1')

    print(nodeInstance.printBinaryTree())
    print(nodeInstance.LCA(1, 6))

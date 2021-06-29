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

    def findPath(self, root, path, k):

        # Baes Case
        if root is None:
            return False

        # Store this node is path vector. The node will be
        # removed if not in path from root to k
        path.append(root.value)

        # See if the k is same as root's key
        if root.value == k:
            return True

        # Check if k is found in left or right sub-tree
        if ((root.left != None and self.findPath(root.left, path, k)) or
                (root.right != None and self.findPath(root.right, path, k))):
            return True

        # If not present in subtree rooted with root, remove
        # root from path and return False

        path.pop()
        return False

    # Returns LCA if node n1 , n2 are present in the given
    # binary tre otherwise return -1
    def findLCA(self, n1, n2):

        # To store paths to n1 and n2 fromthe root
        path1 = []
        path2 = []

        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        if (not self.findPath(self.root, path1, n1) or not self.findPath(self.root, path2, n2)):
            return -1

        # Compare the paths to get the first different value
        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]


if __name__ == "__main__":

    nodeInstance = binaryTree()

    nodeInstance.insertNode('5')
    nodeInstance.insertNode('4')
    nodeInstance.insertNode('6')
    nodeInstance.insertNode('3')
    nodeInstance.insertNode('7')
    nodeInstance.insertNode('2')
    nodeInstance.insertNode('1')

    print('preorder', nodeInstance.printBinaryTree())
    print(nodeInstance.findLCA(1, 1))

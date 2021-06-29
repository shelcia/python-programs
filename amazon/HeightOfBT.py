# Write a Program to Find the Maximum Depth or Height of a Tree

class binaryTreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class binaryTree:

    def __init__(self, root=None):
        self.root = root

    def _insertNode(self, node, value):

        if (value < node.value):
            if(node.left is None):
                node.left = binaryTreeNode(value)
            else:
                self._insertNode(node.left, value)
        elif (value > node.value):
            if(node.right is None):
                node.right = binaryTreeNode(value)
            else:
                self._insertNode(node.right, value)

    def insertNode(self, value):

        node = binaryTreeNode(value)

        if(self.root is None):
            self.root = node
        else:
            self._insertNode(self.root, value)

    def preorderTravesal(self, currentNode):
        if(currentNode is None):
            return []
        else:
            return [currentNode.value] + self.preorderTravesal(currentNode.left) + self.preorderTravesal(currentNode.right)

    def printBT(self):
        if(self.root is None):
            return "empty BT"
        else:
            return self.preorderTravesal(self.root)

    def _maxDepth(self, node):

        if node is None:
            return 0

        else:
            print('node value', node.value)
            lDepth = self._maxDepth(node.left)
            rDepth = self._maxDepth(node.right)

        return max(lDepth, rDepth) + 1

    def maxDepth(self):
        print('maxDepth is called')
        if(self.root is None):
            return "empty BT"
        else:
            self._maxDepth(self.root)


if __name__ == '__main__':

    nodeInstance = binaryTree()

    nodeInstance.insertNode('5')
    nodeInstance.insertNode('7')
    nodeInstance.insertNode('2')
    nodeInstance.insertNode('3')
    nodeInstance.insertNode('8')

    print(nodeInstance.printBT())
    print(nodeInstance.maxDepth())

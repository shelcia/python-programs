class Node:
    # A constructor to create a new Binary tree Node
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def converToMirror(currentNode):

    if(currentNode is None):
        return

    else:

        temp = currentNode

        temp = currentNode.left
        currentNode.left = currentNode.right
        currentNode.right = temp

        converToMirror(currentNode.left)
        converToMirror(currentNode.right)


def inorderTraversal(currentNode):

    if currentNode is None:
        return []

    else:
        return inorderTraversal(currentNode.left) + [currentNode.value] + inorderTraversal(currentNode.right)


# Driver code
if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(inorderTraversal(root))
    converToMirror(root)
    print(inorderTraversal(root))

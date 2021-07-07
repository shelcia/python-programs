# Check whether a binary tree is a full binary tree or not

# A full binary tree is defined as a binary tree in which all nodes have either zero or
# two child nodes. Conversely, there is no node in a full binary tree, which has one child node.
# More information about full binary trees can be found

class Node:

    # Constructor of the node class for creating the node
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# class BinaryTree:

#     def __init__(self, head=None):
#         self.head = head

def checkFullBinaryTree(currentNode):

    if currentNode.left is None and currentNode.right is None:
        return True

    elif currentNode.left is not None and currentNode.right is not None:
        return (checkFullBinaryTree(currentNode.left) and
                checkFullBinaryTree(currentNode.right))

    return False


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.right = Node(40)
    root.left.left = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    root.left.left.left = Node(80)
    root.left.left.right = Node(90)
    root.left.right.left = Node(80)
    root.left.right.right = Node(90)
    root.right.left.left = Node(80)
    root.right.left.right = Node(90)
    root.right.right.left = Node(80)
    root.right.right.right = Node(90)

    if checkFullBinaryTree(root):
        print("The Binary tree is full")
    else:
        print("Binary tree is not full")

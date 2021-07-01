# Write Code to Determine if Two Trees are Identical

# Two trees are identical when they have same data and arrangement of data is also same.

# To identify if two trees are identical, we need to traverse both trees simultaneously,
# and while traversing we need to compare data and children of the trees.

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# class binaryTree:

#     def __init__(self, root=None):
#         self.root = root

def identicalTree(firstTreeNode, secondTreeNode):

    if firstTreeNode is None and secondTreeNode is None:
        return True

    if firstTreeNode is not None and secondTreeNode is not None:

        return (firstTreeNode.value == secondTreeNode.value and
                identicalTree(firstTreeNode.left, secondTreeNode.left) and
                identicalTree(firstTreeNode.right, secondTreeNode.right))


root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

# root2.left = Node(2)
# root2.right = Node(3)
# root2.left.left = Node(4)
# root2.left.right = Node(5)


if(identicalTree(root1, root2)):
    print('Identical Tree')
else:
    print('Non Indentical Trees')

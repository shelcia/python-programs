# There are two types of nodes to be considered.
# 1) Nodes in the subtree rooted with target node. For example if the target node is 8 and k is 2,
# then such nodes are 10 and 14.
# 2) Other nodes, may be an ancestor of target, or a node in some other subtree.
# For target node 8 and k is 2, the node 22 comes in this category.
# Finding the first type of nodes is easy to implement. Just traverse subtrees rooted
# with the target node and decrement k in recursive call. When the k becomes 0,
# print the node currently being traversed (See this for more details).
# Here we call the function as printkdistanceNodeDown().
# How to find nodes of second type? For the output nodes not lying in the subtree
# with the target node as the root, we must go through all ancestors. For every ancestor,
# we find its distance from target node, let the distance be d, now we go to other subtree
# (if target was found in left subtree, then we go to right subtree and vice versa)
# of the ancestor and find all nodes at k-d distance from the ancestor.

#         20
#       /    \
#     8       22
#   /   \
# 4      12
#      /   \
#     10     14


class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def _PrintAllNodes(node, target):

    if node is None and target == 0:
        return None

    if target == 0:
        print(node.data)
        return

    _PrintAllNodes(node.left, target-1)
    _PrintAllNodes(node.right, target-1)


def PrintAllNodes(root, target, k):
    if root is None:
        return

    else:
        targetNode = FindTarget(root, target)
        # print(targetNode)
        _PrintAllNodes(targetNode[0], k)


def PrintAncestors(node, target, k):
    if node is None:
        return
    if k == 0 and node.data == target:
        print()


def FindTarget(node, target):

    if node is None:
        return []

    if node.data == target:
        return [node]

    return FindTarget(node.right, target) + FindTarget(node.left, target)


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right

PrintAllNodes(root, 12, 2)

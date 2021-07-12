# Print all nodes at distance k from a given node


# Given a binary tree, a target node in the binary tree, and an integer value k,
# print all the nodes that are at distance k from the given target node. No parent
# pointers are available.


# Consider the tree shown in diagram
# Input: target = pointer to node with data 8.
# root = pointer to node with data 20.
# k = 2.
# Output : 10 14 22
# If target is 14 and k is 3, then output
# should be “4 20”


# There are two types of nodes to be considered.
# 1) Nodes in the subtree rooted with target node. For example if the target node is 8 and
# k is 2, then such nodes are 10 and 14.
# 2) Other nodes, may be an ancestor of target, or a node in some other subtree.
# For target node 8 and k is 2, the node 22 comes in this category.
# Finding the first type of nodes is easy to implement. Just traverse subtrees rooted
# with the target node and decrement k in recursive call. When the k becomes 0, print
# the node currently being traversed (See this for more details). Here we call the
# function as printkdistanceNodeDown().
# How to find nodes of second type? For the output nodes not lying in the subtree
# with the target node as the root, we must go through all ancestors. For every ancestor,
# we find its distance from target node, let the distance be d, now we go to other subtree
# (if target was found in left subtree, then we go to right subtree and vice versa) of the
# ancestor and find all nodes at k-d distance from the ancestor.

# A binary tree node
class Node:
    # A constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printkDistanceNodeDown(node, k):

    if node is None or k < 0:
        return

    if k == 0:
        print(node.val)
        return

    printkDistanceNodeDown(node.left, k - 1)
    printkDistanceNodeDown(node.right, k - 1)


def printkDistanceNode(root, target, k):

    if root is None:
        return -1

    # if my target itself is root then i just have to find nodes with are at
    # K dist in its subtree alone

    if root == target:
        printkDistanceNodeDown(root, k)
        return 0

    # recrring in left subtre
    dl = printkDistanceNodeDown(root.left, k)

    # Check if target node was found in left subtree
    if dl != -1:

        if dl + 1 == k:
            print(root.val)

        else:
            printkDistanceNodeDown(root.right, k - dl - 2)

        return 1 + dl

    # recrring in right subtree only if we didnt find anything in left subtree
    dr = printkDistanceNodeDown(root.right, k)

    # Check if target node was found in right subtree
    if dr != -1:

        if dr + 1 == k:
            print(root.val)

        else:
            printkDistanceNodeDown(root.right, k - dr - 2)

        return 1 + dr

    return -1


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
printkDistanceNode(root, target, 2)

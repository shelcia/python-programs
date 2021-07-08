# Difference between sums of odd level and even level nodes of a Binary Tree

# Given a a Binary Tree, find the difference between the sum of nodes at odd level and
# the sum of nodes at even level. Consider root as level 1, left and right children of root
# as level 2 and so on.
# For example, in the following tree, sum of nodes at odd level is (5 + 1 + 4 + 8) which is 18.
# And sum of nodes at even level is (2 + 6 + 3 + 7 + 9) which is 27. The output for following
# tree should be 18 – 27 which is -9.


#       5
#     /   \
#    2     6
#  /  \     \
# 1    4     8
#     /     / \
#    3     7   9

class Node:

    # Construct to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def differenceLevels(root):

    oddQueueValues = [root.value]
    evenQueueValues = []
    odd = False

    queue = [root]
    level = []

    while queue != []:

        for node in queue:

            if node.left:
                level.append(node.left)
                if odd:
                    oddQueueValues.append(node.left.value)
                else:
                    evenQueueValues.append(node.left.value)

            if node.right:
                level.append(node.right)
                if odd:
                    oddQueueValues.append(node.right.value)
                else:
                    evenQueueValues.append(node.right.value)

        queue = level
        level = []
        odd = not odd

    print(oddQueueValues, evenQueueValues)

    return sum(oddQueueValues) - sum(evenQueueValues)


if __name__ == '__main__':

    """
    Let us create Binary Tree shown
    in above example """
    root = Node(5)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.left.right.left = Node(3)
    root.right.right = Node(8)
    root.right.right.right = Node(9)
    root.right.right.left = Node(7)

    result = differenceLevels(root)
    print("Diffence between sums is", result)

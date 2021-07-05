# Find maximum level sum in Binary Tree

# Given a Binary Tree having positive and negative nodes, the task is to
# find the maximum sum level in it.

# Examples:

# Input :               4
#                     /   \
#                    2    -5
#                   / \    /\
#                 -1   3 -2  6
# Output: 6
# Explanation :
# Sum of all nodes of 0'th level is 4
# Sum of all nodes of 1'th level is -3
# Sum of all nodes of 0'th level is 6
# Hence maximum sum is 6

# Input :          1
#                /   \
#              2      3
#            /  \      \
#           4    5      8
#                     /   \
#                    6     7
# Output :  17

class Node:

    def __init__(self, key):

        self.value = key
        self.left = None
        self.right = None


def maxLevelSum(root):

    if root is None:
        return

    level = []
    queue = [root]

    sumArray = []

    # root sum
    sumArray.append(root.value)

    while queue != []:
        tempSum = 0
        for node in queue:
            if node.left:
                level.append(node.left)
                tempSum += node.left.value
            if node.right:
                level.append(node.right)
                tempSum += node.right.value

        if level != []:
            sumArray.append(tempSum)
        queue = level
        level = []

    maxIndex = 0
    for i in range(len(sumArray)):
        if sumArray[i] > sumArray[maxIndex]:
            maxIndex = i

    print('sum array', sumArray)
    # print(sumArray)
    print(maxIndex+1)

    return max(sumArray)


# Driver code
if __name__ == '__main__':

    # [-100,-200,-300,-20,-5,-10,null]

    # root = Node(-100)
    # root.left = Node(-200)
    # root.right = Node(-300)
    # root.left.left = Node(-20)
    # root.left.right = Node(-5)
    # root.right.left = Node(-10)

    #            -100
    #            /   \
    #        -200    -300
    #        /  \      \
    #     -20   -5     -10

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    # Constructed Binary tree is:
    #              1
    #            /   \
    #          2      3
    #        /  \      \
    #       4    5      8
    #                 /   \
    #                6     7
    print("Maximum level sum is", maxLevelSum(root))

# Maximum level sum is 17

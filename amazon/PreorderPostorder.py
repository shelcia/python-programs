# Find postorder traversal of BST from preorder traversal

# Given an array representing preorder traversal of BST, print its postorder traversal.

# Examples:

# Input : 40 30 35 80 100
# Output : 35 30 100 80 40

# Input : 40 30 32 35 80 90 100 120
# Output : 35 32 30 120 100 90 80 40

# In pre-order traversal of BST, first element is the root element of the tree.
# Iterate through the given pre-order traversal of BST and compare each element with the
# first element of the array till the index where elements are less than the first element.
# Store the value of the index in a variable called ‘Pivot’. Print elements of a pre-order array
# from ‘Pivot’ index to index 1. Print elements of pre-order array from ‘array, length’ index – 1
# to ‘Pivot’ index + 1. Print first element of pre-order array.


def getPostOrderBST(pre, N):

    pivotPoint = 0
    print('pre', pre)

    # Run loop from 1 to length of pre
    for i in range(1, N):
        if (pre[0] <= pre[i]):
            pivotPoint = i
            break

    print('pivotPoint', pivotPoint)

    # Perform pivot length -1 to zero
    for i in range(pivotPoint - 1, 0, -1):
        print(pre[i], end=" ")

    # Perform end to pivot length
    for i in range(N - 1, pivotPoint - 1, -1):
        print(pre[i], end=" ")
    print(pre[0])


# Driver Code
if __name__ == '__main__':
    pre = [40, 30, 32, 35, 80, 90, 100, 120]
    N = 8

    getPostOrderBST(pre, N)

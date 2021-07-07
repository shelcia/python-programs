# Rearrange a given linked list in-place.

# Given a singly linked list L0 -> L1 -> … -> Ln-1 -> Ln. Rearrange the nodes
# in the list so that the new formed list is : L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 …
# You are required to do this in place without altering the nodes’ values.

# Examples:

# Input:  1 -> 2 -> 3 -> 4
# Output: 1 -> 4 -> 2 -> 3

# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 1 -> 5 -> 2 -> 4 -> 3


# Efficient Solution:

# 1) Find the middle point using tortoise and hare method.
# 2) Split the linked list into two halves using found middle point in step 1.
# 3) Reverse the second half.
# 4) Do alternate merge of first and second halves.

class Node:

    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.next = None


def printlist(node):
    if(node == None):
        return
    while(node != None):
        print(node.value, " -> ", end="")
        node = node.next
    print('None')


def findMiddlePtr(node):

    fastPtr = node.next
    slowPtr = node

    while fastPtr.next is not None:

        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

        if not fastPtr:
            break

    return slowPtr


def reverseList(middlePtr):

    prevNode = None
    currentNode = middlePtr.next
    nextNode = None

    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode

    # head = prevNode
    return prevNode


def rearrange(node):

    middlePtr = findMiddlePtr(node)

    tailNode = reverseList(middlePtr)
    middlePtr.next = None

    printlist(tailNode)

    # temp pointer
    temp = Node(0)
    curr = temp

    while (node != None or tailNode != None):

        # First add the element from first list
        if (node != None):
            curr.next = node
            curr = curr.next
            node = node.next

        # Then add the element from second list
        if(tailNode != None):
            curr.next = tailNode
            curr = curr.next
            tailNode = tailNode.next


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

printlist(head)
rearrange(head)
printlist(head)

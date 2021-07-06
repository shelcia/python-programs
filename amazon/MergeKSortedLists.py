# Merge K sorted linked lists | Set 1

# Given K sorted linked lists of size N each, merge them and print the sorted output.

# Examples:

# Input: k = 3, n =  4
# list1 = 1->3->5->7->NULL
# list2 = 2->4->6->8->NULL
# list3 = 0->9->10->11->NULL

# Output: 0->1->2->3->4->5->6->7->8->9->10->11
# Merged lists in a sorted order
# where every element is greater
# than the previous element.

# Input: k = 3, n =  3
# list1 = 1->3->7->NULL
# list2 = 2->4->8->NULL
# list3 = 9->10->11->NULL

# Output: 1->2->3->4->7->8->9->10->11
# Merged lists in a sorted order
# where every element is greater
# than the previous element.


class Node:
    def __init__(self, value, nexNode=None):
        self.value = value
        self.nextNode = nexNode

# Time Complexity: O(l1+l2+l3...) where l1 and l2 ... are the sizes of linked lists.
# Space Complexity: O(l1+l2+l3+ ...), length of all these nodes


def mergeLists(headA, headB):

    tempNode = Node(-1)
    tail = tempNode

    while True:

        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        # if value in second list lesser than first
        if headA.value <= headB.value:
            tail.nextNode = headA
            headA = headA.nextNode
        # if value in first list lesser than second
        else:
            tail.nextNode = headB
            headB = headB.nextNode

        # move tail pointer progressively
        tail = tail.nextNode

    # print('headA', headA)
    # print('headB', headB)

    # Rest of the elements
    if headA:
        tail.nextNode = headA
        tail = tail.nextNode
    if headB:
        tail.nextNode = headB
        tail = tail.nextNode

    return tempNode.nextNode


def printList(head):

    if head is None:
        return 'Empty List'

    currentNode = head

    while currentNode is not None:
        print(currentNode.value, '->', end=' ')
        currentNode = currentNode.nextNode
    print('None')


if __name__ == "__main__":

    # Number of linked
    # lists
    k = 3

    # an array of pointers
    # storing the head nodes
    # of the linked lists
    arr = [None for i in range(k)]

    arr[0] = Node(1)
    arr[0].nextNode = Node(3)
    arr[0].nextNode.nextNode = Node(5)
    arr[0].nextNode.nextNode.nextNode = Node(7)

    arr[1] = Node(2)
    arr[1].nextNode = Node(4)
    arr[1].nextNode.nextNode = Node(6)
    arr[1].nextNode.nextNode.nextNode = Node(8)

    arr[2] = Node(0)
    arr[2].nextNode = Node(9)
    arr[2].nextNode.nextNode = Node(10)
    arr[2].nextNode.nextNode.nextNode = Node(11)

    print('list1', end=' ')
    printList(arr[0])
    print('list2', end=' ')
    printList(arr[1])
    print('list3', end=' ')
    printList(arr[2])

    for i in range(1, k):
        arr[0] = mergeLists(arr[0], arr[i])
    print('Merged K Sorted Lists')
    printList(arr[0])

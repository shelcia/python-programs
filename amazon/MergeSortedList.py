# Merge two sorted linked lists

# Write a SortedMerge() function that takes two lists, each of which is sorted in
# increasing order, and merges the two together into one list which is in increasing order.
# SortedMerge() should return the new list. The new list should be made by splicing together
# the nodes of the first two lists.

# For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20,
# then SortedMerge() should return a pointer to the head node of the merged list
# 2->3->5->10->15->20.

# There are many cases to deal with: either ‘a’ or ‘b’ may be empty, during processing
# either ‘a’ or ‘b’ may run out first, and finally, there’s the problem of starting the result
# list empty, and building it up while going through ‘a’ and ‘b’.

class Node:
    def __init__(self, value, nexNode=None):
        self.value = value
        self.nextNode = nexNode

# Time Complexity: O(N+M) where N and M are the sizes of linked lists.
# Space Complexity: O(N+M), creating dummy nodes


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insertAtBeginning(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return

        newNode.nextNode = self.head
        self.head = newNode

    def printList(self):

        if self.head is None:
            return 'Empty List'

        currentNode = self.head

        while currentNode is not None:
            print(currentNode.value, '->', end=' ')
            currentNode = currentNode.nextNode
        print('None')


def mergeLists(headA, headB):

    tempNode = Node(0)
    tail = tempNode

    tempList = LinkedList()

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

    # Rest of the elements
    if headA:
        tail.nextNode = headA
        tail = tail.nextNode
    if headB:
        tail.nextNode = headB
        tail = tail.nextNode

    return tempNode.nextNode


if __name__ == "__main__":

    nodeInstance1 = LinkedList()

    nodeInstance1.insertAtBeginning(12)
    nodeInstance1.insertAtBeginning(11)
    nodeInstance1.insertAtBeginning(10)
    nodeInstance1.insertAtBeginning(8)
    nodeInstance1.insertAtBeginning(6)
    nodeInstance1.insertAtBeginning(4)
    nodeInstance1.insertAtBeginning(2)

    nodeInstance1.printList()

    nodeInstance2 = LinkedList()

    nodeInstance2.insertAtBeginning(9)
    nodeInstance2.insertAtBeginning(7)
    nodeInstance2.insertAtBeginning(5)
    nodeInstance2.insertAtBeginning(3)
    nodeInstance2.insertAtBeginning(1)

    nodeInstance2.printList()

    nodeInstance1.head = mergeLists(nodeInstance1.head, nodeInstance2.head)
    print()
    print("Merged Linked List is:")
    nodeInstance1.printList()

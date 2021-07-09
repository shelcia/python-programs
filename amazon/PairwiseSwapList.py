# Pairwise swap elements of a given linked list

# Given a singly linked list, write a function to swap elements pairwise.


# Input : 1->2->3->4->5->6->NULL
# Output : 2->1->4->3->6->5->NULL
# Input : 1->2->3->4->5->NULL
# Output : 2->1->4->3->5->NULL
# Input : 1->NULL
# Output : 1->NULL


# For example, if the linked list is 1->2->3->4->5 then the function should change it
# to 2->1->4->3->5, and if the linked list is then the function should change it to.

class Node:

    # Constructor to initialize the node object
    def __init__(self, value):
        self.value = value
        self.next = None


# just fucking swap the values alone
def PairwiseSwapList(head):

    # reassign the head
    currentNode = head

    while (currentNode and currentNode.next) is not None:

        if currentNode.value != currentNode.next.value:
            currentNode.value, currentNode.next.value = currentNode.next.value, currentNode.value

        currentNode = currentNode.next.next

    return head


def PrintList(head):

    while head is not None:

        print(head.value, '->', end='')
        head = head.next
    print('None')


root = Node(1)
root.next = Node(2)
root.next.next = Node(4)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
PrintList(root)
newHead = PairwiseSwapList(root)
PrintList(newHead)

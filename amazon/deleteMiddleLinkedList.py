# Delete middle of linked list

# Given a singly linked list, delete the middle of the linked list.
# For example, if the given linked list is 1->2->3->4->5 then the linked list
# should be modified to 1->2->4->5

# If there are even nodes, then there would be two middle nodes,
# we need to delete the second middle element. For example,
# if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
# If the input linked list is NULL, then it should remain NULL.

# If the input linked list has 1 node, then this node should be deleted
# and a new head should be returned.


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insertAtBeginning(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        node.nextNode = self.head
        self.head = node

    def deleteMiddle(self):

        if self.head is None or self.head.nextNode is None:
            return

        prevPtr = self.head

        fastPtr = self.head
        slowPtr = self.head

        while fastPtr.nextNode is not None:

            if fastPtr.nextNode.nextNode is None:
                fastPtr = fastPtr.nextNode
            else:
                fastPtr = fastPtr.nextNode.nextNode
            prevPtr = slowPtr
            slowPtr = slowPtr.nextNode
            # nextPtr = slowPtr.nextNode

        prevPtr.nextNode = slowPtr.nextNode
        slowPtr.nexNode = None

    def printList(self):
        if self.head is None:
            print('empty ll')
            return

        currentNode = self.head

        while currentNode is not None:
            print(currentNode.value, '->', end='')
            currentNode = currentNode.nextNode
        print(' None')


if __name__ == '__main__':

    instance = LinkedList()

    instance.insertAtBeginning('1')
    instance.insertAtBeginning('2')
    instance.insertAtBeginning('3')
    instance.insertAtBeginning('4')
    instance.insertAtBeginning('5')
    # instance.insertAtBeginning('6')

    instance.printList()

    instance.deleteMiddle()

    instance.printList()

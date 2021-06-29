# Merge Sort for Linked Lists

# Merge sort is often preferred for sorting a linked list.
# The slow random-access performance of a linked list makes some other algorithms
# (such as quicksort) perform poorly, and others (such as heapsort) completely impossible.

# Let the head by the first node of the linked list be sorted and headRef be the pointer to head. Note that we need a reference to head in MergeSort() as the below implementation changes next links to sort the linked lists (not data at the nodes), so the head node has to be changed if the data at the original head is not the smallest value in the linked list.

# MergeSort(headRef)
# 1) If the head is NULL or there is only one element in the Linked List
#     then return.
# 2) Else divide the linked list into two halves.
#       FrontBackSplit(head, &a, &b); /* a and b are two halves */
# 3) Sort the two halves a and b.
#       MergeSort(a);
#       MergeSort(b);
# 4) Merge the sorted a and b (using SortedMerge() discussed here)
#    and update the head pointer using headRef.
#      *headRef = SortedMerge(a, b);


class linkedListNode:

    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class linkedList:

    def __init__(self, head=None):
        self.head = head

    def insertNode(self, value):

        node = linkedListNode(value)

        if (self.head is None):
            self.head = node
            return

        currentNode = self.head

        while True:
            if(currentNode.nextNode is None):
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printList(self):
        currentNode = self.head

        while(currentNode is not None):
            print(currentNode.value, "->", end="")
            currentNode = currentNode.nextNode
        print('none')

    def middlePointer(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.nextNode
        print(length//2)
        return length//2

    # def splitList(self):
    #     leftMerge = self.head
    #     middle = self.middlePointer()
    #     currentNode = currentNode
    #     for i in range(0, middle):


if __name__ == '__main__':
    nodeCreation = linkedList()
    nodeCreation.insertNode('4')
    nodeCreation.insertNode('5')
    nodeCreation.insertNode('9')
    nodeCreation.insertNode('2')
    nodeCreation.insertNode('6')
    nodeCreation.insertNode('1')
    nodeCreation.printList()
    nodeCreation.middlePointer()

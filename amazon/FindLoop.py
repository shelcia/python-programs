# Detect loop in a linked list

# Given a linked list, check if the linked list has loop or not. Below diagram shows a
# linked list with a loop.


class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):

    if head.next is None:
        return False

    slowPtr = head
    fastPtr = head.next

    while fastPtr.next is not None:

        if slowPtr.val == fastPtr.val:
            return True

        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

    return False


def printList(root):

    cur = root
    while cur is not None:
        print(cur.next, '->')
        cur = cur.next
    print('None')


root = Node(20)
root.next = Node(4)
root.next.next = Node(15)
root.next.next.next = Node(10)
root.next.next.next = root.next

if hasCycle(root):
    print('Loop Detected')
else:
    print('Loop not Detected')

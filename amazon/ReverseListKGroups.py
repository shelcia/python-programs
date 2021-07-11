# Reverse Nodes in k-Group

# Given a linked list, reverse the nodes of a linked list k at a time and return
# its modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end,
# should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(self, head, k):

    # dummy node
    dummyNode = ListNode(-1, head)
    prev = dummyNode
    curr = head

    while curr:
        # tail will start out as curr but reversed
        tail = curr
        idx = 0

        # move k steps forward
        while curr and idx < k:
            curr = curr.next
            idx += 1

        # if it didnt go out of bounds then reverse else connect and break
        if idx == k:
            prev.next = self.reverse_k(tail, k)
            prev = tail
        else:
            prev.next = tail
            # break <<- optional

    return dummyNode.next

# reverse from head until kth index


def reverse_k(head, k):
    prev, curr, nxt = None, head, None
    while curr and k:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt
        k -= 1
    return prev

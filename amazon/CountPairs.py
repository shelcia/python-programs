# Count pairs from two linked lists whose sum is equal to a given value


# Given two linked lists(can be sorted or unsorted) of size n1 and n2 of distinct elements. Given a value x. The problem is to count all pairs from both lists whose sum is equal to the given value x.
# Note: The pair has an element from each linked list.
# Examples:


# Input : list1 = 3->1->5->7
#         list2 = 8->2->5->3
#         x = 10
# Output : 2
# The pairs are:
# (5, 5) and (7, 3)

# Input : list1 = 4->3->5->7->11->2->1
#         list2 = 2->3->4->5->6->8-12
#         x = 9
# Output : 5

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head_ref, new_data):
    new_node = Node(new_data)
    #new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref


def countPairs(head1, head2, targetSum):

    sumList = []
    count = 0

    while head1 is not None:

        if head1.data <= targetSum:
            sumList.append(head1.data)

        head1 = head1.next

    while head2 is not None:

        if targetSum - head2.data in sumList:
            count += 1

        head2 = head2.next

    return count


# Driver program to test above
if __name__ == '__main__':

    head1 = None
    head2 = None

    # create linked list1 3.1.5.7
    head1 = push(head1, 7)
    head1 = push(head1, 5)
    head1 = push(head1, 1)
    head1 = push(head1, 3)

    # create linked list2 8.2.5.3
    head2 = push(head2, 3)
    head2 = push(head2, 5)
    head2 = push(head2, 2)
    head2 = push(head2, 8)

    x = 10

    print("Count = ", countPairs(head1, head2, x))

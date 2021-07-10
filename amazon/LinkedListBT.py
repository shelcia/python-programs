# Construct Complete Binary Tree from its Linked List Representation

# Given Linked List Representation of Complete Binary Tree, construct the Binary tree.
# A complete binary tree can be represented in an array in the following approach.
# If root node is stored at index i, its left, and right children are stored at indices
# 2*i+1, 2*i+2 respectively.
# Suppose tree is represented by a linked list in same way, how do we convert this
# into normal linked representation of binary tree where every node has data, left
# and right pointers? In the linked list representation, we cannot directly access
# the children of the current node unless we traverse the list.

# Linked List node
class ListNode:

    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.next = None

# Binary Tree Node structure


class BinaryTreeNode:

    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def getListValues(self, head):
        cur = head
        res = []
        while cur is not None:
            res.append(cur)
            cur = cur.next
        return res

    def insert(self, node, val):

        print('val', val)

        if node.left is None:
            node.left = BinaryTreeNode(val)
            return

        if node.right is None and node.left is not None:
            node.right = BinaryTreeNode(val)
            return

        if node.left is not None and node.right is not None:
            if node.left.left is not None and node.right.right is not None:
                return self.insert(node.right, val)
            else:
                return self.insert(node.left, val)

    def inorderTraversal(self, currentNode):

        if(currentNode is None):
            return []
        return self.inorderTraversal(currentNode.left) + [currentNode.val] + self.inorderTraversal(currentNode.right)

    def bfs(self):

        level = []
        queue = [self.root]

        print(self.root.val, end=" ")

        while queue != []:
            for node in queue:
                if node.left:
                    level.append(node.left)
                    print(node.left.val, end=" ")
                if node.right:
                    level.append(node.right)
                    print(node.right.val, end=" ")

            queue = level
            level = []
        print('')

    def printBinaryTree(self):

        if self.root is None:
            return []

        return self.inorderTraversal(self.root)

    def linkedListToBT(self, head):

        nodes = self.getListValues(head)

        if self.root is None:
            self.root = BinaryTreeNode(nodes[0].val)

        for ele in nodes[1:]:
            self.insert(self.root, ele.val)


def printList(head):
    cur = head

    while cur is not None:
        print(cur.val, '->', end='')
        cur = cur.next
    print('None')


head = ListNode(10)
head.next = ListNode(12)
head.next.next = ListNode(15)
head.next.next.next = ListNode(25)
head.next.next.next.next = ListNode(30)
head.next.next.next.next.next = ListNode(36)

printList(head)

nodeInstance = BinaryTree()


nodeInstance.linkedListToBT(head)
# print(nodeInstance.printBinaryTree())
print('level order')
nodeInstance.bfs()

# Inorder Traversal of the constructed Binary Tree is:
# 25 12 30 10 36 15

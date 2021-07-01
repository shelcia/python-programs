# Reversing a Queue

# Give an algorithm for reversing a queue Q.
# Only following standard operations are allowed on queue.

# enqueue(x) : Add an item x to rear of queue.
# dequeue() : Remove an item from front of queue.
# empty() : Checks if a queue is empty or not.

# Implementation using queue.Queue
# Queue is built-in module of Python which is used to implement a queue.
# queue.Queue(maxsize) initializes a variable to a maximum size of maxsize.
# A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule.
# There are various functions available in this module:

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue.
# If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty,
# wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot
# is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking.
# If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

from queue import Queue


def printQueue(queue):
    # print(queue.qsize())
    for i in range(queue.qsize()):
        print(queue.queue[i], '<-', end="")

    print()


def reverseQueue(queue):

    stack = []

    while not queue.empty():
        stack.append(queue.queue[0])
        queue.get()

    while len(stack) != 0:
        queue.put(stack[-1])  # stack[-1] is the last eleemnt
        stack.pop()


if __name__ == '__main__':
    queue = Queue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    queue.put(40)
    queue.put(50)
    queue.put(60)
    queue.put(70)
    queue.put(80)
    queue.put(90)
    queue.put(100)
    printQueue(queue)
    reverseQueue(queue)
    printQueue(queue)

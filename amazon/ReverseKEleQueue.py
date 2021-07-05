# Reversing the first K elements of a Queue


# Given an integer k and a queue of integers, we need to reverse the order of the first k elements of the queue, leaving the other elements in the same relative order.
# Only following standard operations are allowed on queue.

# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.


from queue import Queue


def reverseElementsQueue(Queue, k):

    if (Queue.empty() or k > Queue.qsize()):
        return
    if (k <= 0):
        return

    Stack = []

    # put the first K elements
    # into a Stack
    for i in range(k):
        Stack.append(Queue.queue[0])
        Queue.get()

    # Enqueue the contents of stack
    # at the back of the queue
    while (len(Stack) != 0):
        Queue.put(Stack[-1])
        Stack.pop()

    # Remove the remaining elements and
    # enqueue them at the end of the Queue
    for i in range(Queue.qsize() - k):
        Queue.put(Queue.queue[0])
        # print('inter', Queue.queue[0], i)
        Queue.get()


def printQueue(queue):

    for i in range(queue.qsize()):
        print(queue.queue[i], end=" ")
        if i != queue.qsize()-1:
            print('<-', end=" ")

    print()


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
    reverseElementsQueue(queue, 5)
    printQueue(queue)

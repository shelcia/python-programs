# An Interesting Method to Generate Binary Numbers from 1 to n

# Given a number n, write a function that generates and
# prints all binary numbers with decimal values from 1 to n.


import queue


def PrintBinary(n):
    # print(n)

    from queue import Queue

    q = Queue()

    q.put('1')

    while n > 0:

        n -= 1

        s1 = q.get()
        print(s1, end=',')

        s2 = s1

        q.put(s1 + '0')
        q.put(s2 + '1')
    print()


if __name__ == "__main__":
    PrintBinary(10)

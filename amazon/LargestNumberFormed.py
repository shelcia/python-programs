# Given an array of numbers, arrange them in a way that yields the largest value.
# For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654
# gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4},
# then the arrangement 998764543431 gives the largest value.


# map() function returns a map object(which is an iterator) of the results after
# applying the given function to each item of a given iterable (list, tuple etc.)

# Syntax :
# map(fun, iter)
# Parameters :

# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

# NOTE : You can pass one or more iterable to the map() function.

from itertools import permutations

# Time Complexity -> O(nlogn) Space Complexity -> O(1)

# Time exceeded in Leet Code


def largest(l):
    lst = []

    for i in permutations(l, len(l)):
        # provides all permutations of the list values,
        # store them in list to find max
        # print('index', i)
        lst.append("".join(map(str, i)))
        # print('list', lst)
    return max(lst)

# def largestFormed(arr):


print(largest([54, 546, 548, 60]))  # Output 6054854654

# Given an array of numbers, arrange them in a way that yields the largest value.
# For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654
# gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4},
# then the arrangement 998764543431 gives the largest value.


from itertools import permutations

# Time Complexity -> O(nlogn) Space Complexity -> O(1)


def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        # provides all permutations of the list values,
        # store them in list to find max
        print('index', i)
        lst.append("".join(map(str, i)))
        print('list', lst)
    return max(lst)


print(largest([54, 546, 548, 60]))  # Output 6054854654

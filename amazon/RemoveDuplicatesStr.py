# Remove duplicates from a given string


# Given a string S, the task is to remove all the duplicates in the given string.
# Below are the different methods to remove duplicates in a string.


def removeDuplicates(string):

    arr = list(string)
    arr = set(arr)

    print(''.join(arr))


removeDuplicates('eeeefggkkorss')

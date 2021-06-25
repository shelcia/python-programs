# The join() method is a string method and returns a string in which the elements
# of sequence have been joined by str separator.

# Syntax:

# string_name.join(iterable)

# string_name: It is the name of string in which
#              joined elements of iterable will be
#              stored.
# Parameters: The join() method takes iterable – objects capable of returning its
# members one at a time. Some examples are List, Tuple, String, Dictionary and Set

# Return Value: The join() method returns a string concatenated with the elements of iterable.

# Type Error: If the iterable contains any non-string values, it raises a TypeError exception.


def methodOne(string):
    return string[::-1]


def methodTwo(string):
    arr = list(string)
    arr.reverse()
    reversed_str = "".join(arr)
    return reversed_str


if __name__ == '__main__':
    string = 'shelcia'
    print(methodOne(string))
    print(methodTwo(string))

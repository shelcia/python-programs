# String containing first letter of every word in a given string with spaces
#
# String str is given which contains lowercase English letters and spaces.
# It may contain multiple spaces. Get the first letter of every word and
# return the result as a string. The result should not contain any space.

def FirstLetterPrint(string):

    arr = list(map(str, string.split(' ')))
    # print(arr)

    for ele in arr:
        print(ele[0], end='')
    print()


string = 'I am a joke'
FirstLetterPrint(string)

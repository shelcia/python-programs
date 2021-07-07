# Word Break Problem

# Given an input string and a dictionary of words, find out if the input string can be
# segmented into a space-separated sequence of dictionary words. See following examples for
# more details.
# This is a famous Google interview question, also being asked by many other companies now a days.

# Consider the following dictionary
# { i, like, sam, sung, samsung, mobile, ice,
#   cream, icecream, man, go, mango}

# Input:  ilike
# Output: Yes
# The string can be segmented as "i like".

# Input:  ilikesamsung
# Output: Yes
# The string can be segmented as "i like samsung"
# or "i like sam sung".


# The any() function is an inbuilt function in Python which returns true if any of the
# elements of a given iterable( List, Dictionary, Tuple, set, etc) are True else it returns False.

# Syntax: any(iterable)


# Parameters: Iterable: It is an iterable object such as a dictionary, tuple, list, set, etc.

def wordBreak(wordList, word):

    print('this recursive runs!!')

    if word == '':
        print('i ran')
        return True
    else:
        print('word', word)
        wordLen = len(word)
        return (any([(word[:i] in wordList) and
                     wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]))


wordList = ["mobile", "samsung", "sam", "sung",
            "man", "mango", "icecream", "and",
            "go", "i", "like", "ice", "cream"]

word = "ilikesamsung"

print(wordBreak(wordList, word))

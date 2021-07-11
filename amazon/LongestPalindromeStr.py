# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),


def longestAtIndex(s, l, r):

    # check if it goes out of bound or
    # they are not palindrome anymore
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r -= 1

    r += 1

    return (r-l+1, l, r)


def longestPalindrome(s):

    longest = 0
    left, right = 0, -1

    for i in range(len(s)):

        # for odd characters
        length, l, r = longestAtIndex(s, i, i)

        if length > longest:
            longest = length
            left = l
            right = r

        # for even characters
        length, l, r = longestAtIndex(s, i, i + 1)

        if length > longest:
            longest = length
            left = l
            right = r

    # print(left, right+1)
    print(length)
    print(s[left: right + 1])


longestPalindrome("babad")
# longestPalindrome("cbbd")

# Time complexity -> O(n2)

# def longestPalindrome(s):

#     res = ""
#     resLen = 0
#     for i in range(len(s)):
#         # odd length
#         l, r = i, i
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if (r - l + 1) > resLen:
#                 res = s[l:r+1]
#                 resLen = r - l + 1
#             l -= 1
#             r += 1
#         # even length
#         l, r= i, i + 1
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if (r - l + 1) > resLen:
#                 res = s[l:r+1]
#                 resLen = r - l + 1
#             l -= 1
#             r += 1

#     return res


# longestPalindrome("babad")
# longestPalindrome("cbbd")

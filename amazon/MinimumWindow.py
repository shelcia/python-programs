# Minimum Window Substring

# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in
# t (including duplicates) is included in the window. If there is no such substring,
# return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.


# Follow up: Could you find an algorithm that runs in O(m + n) time?

def minWindow(s, t):

    if t == "":

        return t

    req, cur = {}, {}

    for c in t:
        req[c] = 1 + req.get(c, 0)

    have, need = 0, len(req)
    res, resLen = [-1, -1], float("infinity")

    l = 0
    for r in range(len(s)):
        c = s[r]
        cur[c] = 1 + cur.get(c, 0)

        if c in req and cur[c] == req[c]:
            have += 1

        while have == need:
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            # pop from left of the array
            cur[s[l]] -= 1

            if s[l] in cur and cur[s[l]] < req[s[l]]:
                have -= 1
            l += 1

    l, r = res

    return s[l:r+1] if resLen != float("infinity") else ""

    # req = {}
    # cur = {}

    # for c in t:
    #     if c not in req:
    #         req[c] = 1
    #     else:
    #         req[c] += 1

    # start = 0
    # end = len(list(s))

    # min_length = -1
    # candidates = []

    # while start < end - len(t):

    #     print(s[start: end])

    #     for c in s[start: end]:
    #         print(c, cur)
    #         if c in req.keys():
    #             if c in cur:
    #                 cur[c] += 1
    #             else:
    #                 cur[c] = 1
    #         if cur == req:
    #             candidates.append(s[start: end])

    #     start += 1

    # start += 1
    # for key in req.keys():
    #     if req[key] < cur[key]:
    #         print('yes eligible')

    # min_length = end - start

    print(req)
    # print(cur)


minWindow("ADOBECODEBANC", "ABC")

minWindow("DEBANC", "ABC")

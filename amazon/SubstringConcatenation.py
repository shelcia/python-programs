# Substring with Concatenation of All Words

# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of each word
# in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]


# Constraints:

# 1 <= s.length <= 104
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.


def findSubstring(s, words):

    # eliminating redundant words
    # words = list(set(words))
    window = 0
    res = []

    for ele in words:
        window += len(ele)

    # print(window)
    if len(s) < window:
        return []

    start, end = 0, window

    while end <= len(s):

        substring = True

        redundantWords = {}

        for ele in words:
            if words.count(ele) != 1:
                if ele not in redundantWords:
                    redundantWords[ele] = 1
                else:
                    redundantWords[ele] += 1

            if ele not in s[start:end]:
                substring = not substring
                break
            # if words.count(ele) == 1:

        if substring:
            # print('substring candidate', s[start:end])
            if (redundantWords):
                for key in redundantWords:
                    temp = s[start:end].replace(key, '', 1)
                    for i in range(1, redundantWords[key]):
                        # print('temp', temp)
                        if key not in temp:
                            # print('i executed')
                            substring = not substring
                            break
                        temp = temp.replace(key, '', 1)
                if substring:
                    res.append(start)

            else:

                res.append(start)

        start, end = start + 1, end + 1

    print(res)


findSubstring("barfoothefoobarman", ["foo", "bar"])  # [0,9]
findSubstring("wordgoodgoodgoodbestword", [
              "word", "good", "best", "word"])  # []
findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])  # [6,9,12]
findSubstring("wordgoodgoodgoodbestword", [
              "word", "good", "best", "word"])  # []
findSubstring("wordgoodgoodgoodbestwordword", [
              "word", "good", "best", "word"])  # [12]
findSubstring("wordgoodgoodgoodbestwordword", [
              "word", "good", "best", "word", "word"])  # []
findSubstring("wordgoodgoodgoodbestwordwordword", [
              "word", "good", "best", "word", "word"])  # []


# Efficient LEetcode Soln.

# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:

#         if not s or not words:
#             return []

#         count = {}
#         for word in words:
#             count[word] = count.get(word,0) + 1

#         lw = len(words[0])
#         fin = []

#         for i in range(lw):
#             l = r = i
#             window = {}

#             while r < len(s):
#                 curr_w = s[r:r+lw]

#                 if curr_w not in count:
#                     window.clear()
#                     r += lw
#                     l = r
#                 else:
#                     window[curr_w] = window.get(curr_w,0) + 1

#                     if window[curr_w] <= count[curr_w]:
#                         r += lw

#                     else:
#                         while l <= r and window[curr_w]>count[curr_w]:
#                             w = s[l:l+lw]
#                             window[w] -= 1
#                             l += lw
#                         r += lw
#                 if window == count:
#                     fin.append(l)
#         return fin

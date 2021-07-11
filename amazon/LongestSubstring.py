

def lengthOfLongestSubstring(s: str) -> int:

    if s == "":
        return 0

    hashset = set()

    l, r = 0, 0

    max_so_far = 0

    for r in range(len(s)):

        while s[r] in hashset:
            print('begin', hashset, l, r)
            hashset.remove(s[l])
            print('later', hashset, l, r)
            l += 1

        # useless
        # if s[r] in hashset:
        #     hashset.clear()
        #     print(hashset)
        #     l = r

        hashset.add(s[r])

        max_so_far = max(max_so_far, r - l + 1)

    return max_so_far


print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
print(lengthOfLongestSubstring("dvdf"))  # 3
# print(lengthOfLongestSubstring(""))  # 0

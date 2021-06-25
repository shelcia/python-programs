
def groupAnagrams(words):

    # SORT ALL WORDS
    list = [''.join(sorted(word)) for word in words]

    dict = {}
    for i in range(len(list)):
        dict.setdefault(list[i], []).append(i)

    for key, value in dict.items():
        print([words[v] for v in value])


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groupAnagrams(words)

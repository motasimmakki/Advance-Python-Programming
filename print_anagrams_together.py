def Anagrams(words, n):
    originalWords = []
    i = 0
    while i < n:
        originalWords.append(words[i])
        i += 1
    # print(originalWords)
    
    i = 0
    while i < n:
        words[i] = ''.join(sorted(words[i]))
        i += 1
    # print(words)
    
    mappedIndex = {}
    i = 0
    while(i < len(words)):
        if words[i] not in mappedIndex:
            mappedIndex[words[i]] = [originalWords[i]]
        else:
            mappedIndex[words[i]].append(originalWords[i])
        i += 1
    # print(mappedIndex)
    
    groupedAnagrams = []
    for key in mappedIndex.keys():
        groupedAnagrams.append(mappedIndex[key])
    # print(groupedAnagrams)
    
    return groupedAnagrams

# Test Case: 01
# N = 5
# words = ["act", "god", "cat", "dog", "tac"]

# Test Case: 02
N = 3
words = ["no", "on", "is"]

print(Anagrams(words, N))
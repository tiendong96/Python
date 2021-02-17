#Check if two string arrays are equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

word1 = ["ab", "c"]
word2 = ["a", "bc"]

newWord1 = ''.join(word1)
newWord2 = ''.join(word2)

if newWord1 == newWord2:
    return True
return False

# Runtime: 28 ms, faster than 92.05% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 14.3 MB, less than 34.39% of Python3 online submissions for Check If Two String Arrays are Equivalent.
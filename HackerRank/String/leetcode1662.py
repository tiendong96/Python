#Check if two string arrays are equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

word1 = ["ab", "c"]
word2 = ["a", "bcsdf"]

newWord1 = ''.join(word1)
newWord2 = ''.join(word2)

if newWord1 == newWord2:
    print("true")
else:
    print("nah")
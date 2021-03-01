class Solution:
    def countConsistentStrings(allowed, words) -> int:
        return sum(all(char in allowed for char in words) for word in words)


    if __name__ == '__main__':
        allowed = "ab"
        words = ["ad", "bd", "aaab", "baa", "badab"]
        print(countConsistentStrings(allowed, words))
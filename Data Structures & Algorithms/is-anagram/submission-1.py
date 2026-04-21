class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = [0] * 26
        d2 = [0] * 26
        for i in range(len(s)):
            d1[ord(s[i]) - ord('a')] += 1
            d2[ord(t[i]) - ord('a')] += 1
        return d1 == d2
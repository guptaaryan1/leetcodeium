class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cs = set()
        maxlen = 0
        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l += 1
            cs.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen
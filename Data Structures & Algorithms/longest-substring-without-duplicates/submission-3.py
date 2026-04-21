class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currset = set()
        l, r = 0, 1
        res = 0
        for r in range(len(s)):
            while s[r] in currset:
                currset.remove(s[l])
                l += 1
            currset.add(s[r])
            res = max(res, r - l + 1)
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        res = 0
        maxf = 0
        freq[ord(s[0]) - ord('A')] += 1
        if len(s) == 1:
            return 1
        for r in range(1, len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, freq[ord(s[r]) - ord('A')])
            while (r - l + 1) - maxf > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(r-l+1, res)
        return res
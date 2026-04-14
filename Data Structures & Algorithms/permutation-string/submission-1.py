class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2) < len(s1)):
            return False
        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1

        for i in range(0, len(s2) - len(s1) + 1):
            print(i, freq)
            ftmp = [0] * 26
            for c in s2[i:i + len(s1)]:
                ftmp[ord(c) - ord('a')] += 1
            if (ftmp == freq):
                return True
        return False


        
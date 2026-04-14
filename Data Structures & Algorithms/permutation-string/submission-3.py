class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2) < len(s1)):
            return False
        freq = [0] * 26
        freq1 = [0] * 26
        matches = 0 
        for c in range(len(s1)):
            freq[ord(s1[c]) - ord('a')] += 1
            freq1[ord(s2[c]) - ord('a')] += 1
        for i in range(26):
            if (freq1[i] == freq[i]):
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            freq1[index] += 1
            if freq1[index] == freq[index]:
                matches += 1
            elif freq[index] + 1 == freq1[index]:
                matches -= 1
            index = ord(s2[l]) - ord('a')
            freq1[index] -= 1
            if freq1[index] == freq[index]:
                matches += 1
            elif freq[index] - 1 == freq1[index]:
                matches -= 1
            l += 1

        return matches == 26


        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        d = defaultdict(list)
        for string in strs:
            freq = [0] * 26
            for c in string:
                freq[ord(c) - ord('a')] += 1
            d[tuple(freq)].append(string)
        return list(d.values())

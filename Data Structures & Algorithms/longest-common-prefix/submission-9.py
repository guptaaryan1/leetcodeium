class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        while i < len(strs[0]):
            cur = strs[0][i]
            for st in strs:
                if i >= len(st) or st[i] != cur:
                    return res
            if len(st) > i and st != "":
                res += cur
            i += 1
        return res
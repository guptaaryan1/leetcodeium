class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += "#"
            res += string
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            startofnum = i
            print(startofnum)

            while (s[i].isdigit()):
                i += 1
            size = int(s[startofnum:i])
            print(size, i)
            print(s[i+1: i + 1 + size])
            res.append(s[i + 1: i + 1 + size])
            i += size + 1
        return res
# 5#hello5#world
                

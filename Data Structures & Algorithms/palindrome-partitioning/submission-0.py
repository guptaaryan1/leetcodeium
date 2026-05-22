class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        p = []
        def dfs(i):
            if (i == len(s)):
                res.append(p.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    p.append(s[i:j + 1])
                    dfs(j + 1)
                    p.pop()
        dfs(0)
        return res
    def isPali(self, st, l, r):
        while l < r:
            if (st[l] != st[r]):
                return False
            l, r = l + 1, r - 1
        return True
            
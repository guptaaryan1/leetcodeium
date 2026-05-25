class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        
        visit = [False] * n
        l = [[] for _ in range(n)]
        for s, e in edges:
            l[s].append(e)
            l[e].append(s)
        def dfs(node):
            for neighbor in l[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
        return res
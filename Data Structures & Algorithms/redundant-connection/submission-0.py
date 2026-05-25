class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        alist = [[] for _ in range(len(edges) + 1)]
        visit = set()
        def dfs(node, parent):
            if node == e:
                return False
            if node in visit:
                return False
            visit.add(node)
            for nei in alist[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        for s, e in edges:
            visit = set()
            if not dfs(s, -1):
                return [s, e]
            alist[s].append(e)
            alist[e].append(s)
        return []
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        cycle = set()
        mapping = {i: [] for i in range(n)}
        for start, end in edges:
            mapping[start].append(end)
            mapping[end].append(start)
        def dfs(node, par):
            if node in cycle:
                return False
            cycle.add(node)
            for neigh in mapping[node]:
                if neigh == par:
                    continue
                if not dfs(neigh, node):
                    return False
            return True


        return dfs(0, -1) and len(cycle) == n
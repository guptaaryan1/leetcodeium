class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class DisjointSet:
            def __init__(self, n) -> None:
                self.rank = [0] * (n + 1)
                self.parent = [i for i in range(n + 1)]
                pass
            def findParent(self, node):
                if self.parent[node] == node:
                    return node
                self.parent[node] = self.findParent(self.parent[node])
                return self.parent[node]
            def union(self, u, v):
                upu = self.findParent(u)
                upv = self.findParent(v)
                if self.rank[upu] > self.rank[upv]:
                    self.parent[upv] = upu
                elif self.rank[upu] < self.rank[upv]:
                    self.parent[upu] = upv
                else:
                    self.parent[upu] = upv
                    self.rank[upv] += 1
        ds = DisjointSet(n)
        for src, dst in edges:
            ds.union(src, dst)
        roots = set()
        for i in range(n):
            roots.add(ds.findParent(i))
        return len(roots)

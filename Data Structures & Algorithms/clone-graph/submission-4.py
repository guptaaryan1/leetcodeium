"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        dic = {}
        

        def dfs(node):
            if not node:
                return None

            if node in dic:
                return dic[node]
            copy = Node(node.val)
            dic[node] = copy
            for neighbor in node.neighbors:
                dic[node].neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None
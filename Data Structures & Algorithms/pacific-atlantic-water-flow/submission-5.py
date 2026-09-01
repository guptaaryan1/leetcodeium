class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, visited):
            if ((r, c) in visited):
                return False, False
            visited.add((r, c))
            pacific = r == 0 or c == 0
            atlantic = r == rows - 1 or c == cols - 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[r][c]):
                    p, a = dfs(nr, nc, visited)
                    pacific = p or pacific
                    atlantic = a or atlantic
            return pacific, atlantic
        res = []

        for r  in range(rows):
            for c in range(cols):
                p, a = dfs(r, c, set())
                if p and a:
                    res.append([r, c])
        return res
            

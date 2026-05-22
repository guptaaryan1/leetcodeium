class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c, area):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                r, c = q.popleft()
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    if ((r + dr) in range(rows) and
                        (c + dc) in range(cols) and
                        grid[r + dr][c + dc] == 1 and
                        (r + dr, c + dc) not in visited):
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                        area += 1

            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 1
                    area = bfs(r, c, area)
                    res = max(res, area)
        return res

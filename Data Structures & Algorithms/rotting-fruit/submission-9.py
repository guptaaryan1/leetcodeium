class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        q = deque()
        fresh = 0
        def addNeighbors(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] != 1):
                return
            nonlocal fresh
            visited.add((r, c))
            q.append([r, c])
            fresh -= 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        t = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addNeighbors(r + 1, c)
                addNeighbors(r - 1, c)
                addNeighbors(r, c + 1)
                addNeighbors(r, c - 1)
            t += 1
        return t if not fresh else -1


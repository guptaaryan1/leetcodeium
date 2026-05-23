class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if grid == [[0]]:
            return 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        time = -1
        def validNeighbor(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] == 0 or grid[r][c] == 2):
                return
            visited.add((r, c))
            q.append([r, c])
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                validNeighbor(r + 1, c)
                validNeighbor(r - 1, c)
                validNeighbor(r, c + 1)
                validNeighbor(r, c - 1)
            time += 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return time

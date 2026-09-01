class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for i in range(m)]

        def dfs(r, c):
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            left = dfs(r, c - 1)
            up = dfs(r - 1, c)
            memo[r][c] = left + up
            return left + up
        return dfs(m - 1, n - 1)


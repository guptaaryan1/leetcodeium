class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def dfs(n):
            if n == 1:
                return 1

            if n == 2:
                return 2
            
            if memo[n] != -1:
                return memo[n]
            val = dfs(n - 1) + dfs(n - 2)
            memo[n] = val
            return val
        return dfs(n)
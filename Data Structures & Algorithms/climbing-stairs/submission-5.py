class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        memo[0] = 1
        memo[1] = 1
        # def dfs(i):
        #     if i == 0 or i == 1:
        #         return 1
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = dfs(i - 1) + dfs(i - 2)
        #     return dfs(i - 1) + dfs(i - 2)
        # return dfs(n)
        for i in range(2, n + 1):

            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]
            
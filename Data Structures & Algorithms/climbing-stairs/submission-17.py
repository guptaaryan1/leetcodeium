class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        # def dfs(n):
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     if memo[n] != -1:
        #         return memo[n]
        #     val = dfs(n - 1) + dfs(n - 2)
        #     memo[n] = val
        #     return val
        # return dfs(n)
        if n == 1:
            return 1
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n + 1):
            val = memo[i - 1] + memo[i - 2]
            memo[i] = val
            print(memo)
        return memo[n]




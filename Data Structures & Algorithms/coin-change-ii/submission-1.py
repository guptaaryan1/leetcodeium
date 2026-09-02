class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, sub, subSum):
            if subSum > amount or i >= len(coins):
                return 0
            if subSum == amount:
                return 1
            if (i, subSum) in memo:
                return memo[(i, subSum)]

            
            sub.append(coins[i])
            including = dfs(i, sub, subSum + coins[i])
            sub.pop()
            excluding = dfs(i + 1, sub, subSum)
            memo[(i, subSum)] = including + excluding
            return including + excluding
        return dfs(0, [], 0)

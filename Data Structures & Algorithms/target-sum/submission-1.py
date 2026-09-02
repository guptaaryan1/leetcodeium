class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, curSum):
            if curSum == target and i == len(nums):
                return 1
            elif i == len(nums):
                return 0
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            left = dfs(i + 1, curSum + nums[i])
            right = dfs(i + 1, curSum - nums[i])
            memo[(i, curSum)] = left + right
            return left + right
        return dfs(0, 0)
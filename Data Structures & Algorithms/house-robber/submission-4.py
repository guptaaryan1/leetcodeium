class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums) + 1)
        def dfs(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            if memo[i] != -1:
                return memo[i]
            
            rob = nums[i] + dfs(i - 2)
            norob = dfs(i - 1)
            memo[i] = max(rob, norob)
            return memo[i]
        return dfs(len(nums) - 1)
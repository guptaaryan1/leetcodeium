class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums))
        def dfs(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[i])
            if memo[i] != -1:
                return memo[i]
            werob = nums[i] + dfs(i - 2)
            wedontrob = dfs(i - 1)
            memo[i] = max(werob, wedontrob)
            return max(werob, wedontrob)
        
        return dfs(len(nums) - 1)
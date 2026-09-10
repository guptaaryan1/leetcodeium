class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums))
        # def dfs(i):
        #     if i == 0:
        #         return nums[i]
        #     if i == 1:
        #         return max(nums[0], nums[i])
        #     if memo[i] != -1:
        #         return memo[i]
        #     werob = nums[i] + dfs(i - 2)
        #     wedontrob = dfs(i - 1)
        #     memo[i] = max(werob, wedontrob)
        #     return max(werob, wedontrob)
        # return dfs(len(nums) - 1)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            werob = nums[i] + memo[i - 2]
            wedontrob = memo[i - 1]
            memo[i] = max(werob, wedontrob)
        return memo[len(nums) - 1]


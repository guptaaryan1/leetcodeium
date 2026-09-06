class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = [-1] * (len(nums))
        # def dfs(i):
        #     if i == 0:
        #         return nums[i]
        #     if i == 1:
        #         return max(nums[0], nums[1])
        #     if memo[i] != -1:
        #         return memo[i]
            
        #     rob = nums[i] + dfs(i - 2)
        #     norob = dfs(i - 1)
        #     memo[i] = max(rob, norob)
        #     return memo[i]
        # return dfs(len(nums) - 1)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        one = nums[0]
        two = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # rob = nums[i] + memo[i - 2]
            # norob = memo[i - 1]
            # memo[i] = max(rob, norob)
            # one -> memo[i - 1]
            # two -> nums[i] + one
            one, two = two, max(nums[i] + one, two)
        return two
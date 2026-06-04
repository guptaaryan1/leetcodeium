class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if sum(cur) > target or i >= len(nums):
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            
            cur.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur)
        dfs(0, [])
        return res
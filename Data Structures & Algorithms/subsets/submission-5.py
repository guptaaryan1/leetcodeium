class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = []
        def dfs(i):
            if i >= len(nums):
                res.append(l.copy())
                return
            l.append(nums[i])
            dfs(i + 1)
            l.pop()
            dfs(i + 1)
        dfs(0)
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, l):
            if i == len(nums):
                res.append(l.copy())
                return
            l.append(nums[i])
            dfs(i + 1, l)
            l.pop()
            dfs(i + 1, l)
        dfs(0, [])
        return res
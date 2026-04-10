class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # left = [1 for i in range(n)]
        # right = [1 for i in range(n)]
        # pl = 1
        # pr = 1
        # for i in range(n):
        #     if (i == 0):
        #         continue
        #     left[i] = nums[i - 1] * pl
        #     pl = nums[i - 1] * pl
        # for i in range(n - 1, -1, -1):
        #     if (i == n - 1):
        #         continue
        #     right[i] = nums[i + 1] * pr
        #     pr = nums[i + 1] * pr
        # return [left[i] * right[i] for i in range(n)]
        pre = 1
        post = 1
        res = [1 for i in range(n)]
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        for num in range(n - 1, -1, -1):
            res[num] = res[num] * post
            post = nums[num] * post
        return res

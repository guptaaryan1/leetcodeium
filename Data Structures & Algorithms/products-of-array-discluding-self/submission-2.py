class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        cumprod = 1
        for i, num in enumerate(nums):
            res[i] *= cumprod
            cumprod *= num
        doublecumprod = 1
        for  i in range(len(nums) - 1, -1, -1):
            res[i] *= doublecumprod
            doublecumprod *= nums[i]
        return res
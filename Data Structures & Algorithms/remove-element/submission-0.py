class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] == val:
                c += 1
        for i in range(c):
            nums.remove(val)
        return len(nums)
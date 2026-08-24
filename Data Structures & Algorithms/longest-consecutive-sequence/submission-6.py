class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            maxLen = 0
            if (num - 1) not in numSet:
                while (num + maxLen) in numSet:
                    maxLen += 1
            res = max(res, maxLen)
        return res
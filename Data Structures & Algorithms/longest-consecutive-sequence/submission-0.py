class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        s = set(nums)
        for num in nums:
            if num - 1 not in s:
                length = 1
                while num + 1 in s:
                    length += 1
                    num = num + 1
                maxlen = max(maxlen, length)
        return maxlen
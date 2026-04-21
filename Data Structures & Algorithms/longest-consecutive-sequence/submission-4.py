class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlen = 0
        for num in nums:
            if num - 1 not in s:
                length = 0
                while num + length in s:
                    length += 1
                maxlen = max(maxlen, length)
                
                    
             
        return maxlen
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for k, v in d.items():
            if v > 1:
                return True
        return False
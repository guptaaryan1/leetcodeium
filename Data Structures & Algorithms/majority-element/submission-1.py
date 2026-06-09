class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        f = 0
        res = 0
        for k, v in d.items():
            if f < v:
                res = k
                f = v
        return res
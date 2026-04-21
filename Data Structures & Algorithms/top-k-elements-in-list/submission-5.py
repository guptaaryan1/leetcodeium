class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = {}
        res = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num, cnt in counts.items():
            freq[cnt].append(num)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


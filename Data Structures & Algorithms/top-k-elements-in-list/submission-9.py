class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [[] for i in range(len(nums) + 1)]
        d = Counter(nums)
        print(d)
        for key, val in d.items():
            print(key, val)
            l[val].append(key)
            print(l[val], l)
        res = []
        for i in range(len(l) - 1, -1, -1):
            if k == 0:
                return res
            while (len(l[i]) > 0 and k > 0):
                res.append(l[i].pop())
                k -= 1
        return res
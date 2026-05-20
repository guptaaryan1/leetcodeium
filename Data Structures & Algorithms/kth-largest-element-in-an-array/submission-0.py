class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newnums = [-num for num in nums]
        heapq.heapify(newnums)
        res = 0
        while k > 0:
            res = heapq.heappop(newnums)
            k -= 1
        return -res
        
            
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            # if (len(maxheap) >= 2):

            s1 = heapq.heappop(maxheap)
            s2 = heapq.heappop(maxheap)
            diff = abs(s2 - s1)
            heapq.heappush(maxheap, -diff)
        return -maxheap[0]

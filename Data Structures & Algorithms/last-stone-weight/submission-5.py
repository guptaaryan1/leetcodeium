class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)
        while len(h) > 1:
            stone1 = -heapq.heappop(h)
            stone2 = -heapq.heappop(h)
            newStone = abs(stone2 - stone1)
            heapq.heappush(h, -newStone)
        return -h[0]

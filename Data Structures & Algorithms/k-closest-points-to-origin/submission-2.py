class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for x, y in points:
            dist = (x * x) + (y * y)
            heap.append([dist, x, y])
        heapq.heapify(heap)
        for i in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res
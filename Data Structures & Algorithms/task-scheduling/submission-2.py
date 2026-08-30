class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        q = deque()
        heap = [-x for x in c.values()]
        heapq.heapify(heap)
        t = 0
        while heap or q:
            t += 1
            if heap:
                f = heapq.heappop(heap)
                f += 1
                if f:
                    q.append([f, t + n])
            if q and q[0][1] == t:
                heapq.heappush(heap, q.popleft()[0])
        return t
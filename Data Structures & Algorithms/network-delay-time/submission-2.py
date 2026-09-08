class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for i in range(n + 1)]
        adj = [[] for i in range(n + 1)]
        heap = [] # (d, node)
        for src, dst, t in times:
            adj[src].append((dst, t))
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            d, node = heapq.heappop(pq)
            for nei, ndst in adj[node]:
                if ndst + dist[node] < dist[nei]:
                    dist[nei] = ndst + dist[node]
                    heapq.heappush(pq, (dist[nei], nei))
        return max(dist[1:]) if max(dist[1:]) != float("inf") else -1
            
        
        
        
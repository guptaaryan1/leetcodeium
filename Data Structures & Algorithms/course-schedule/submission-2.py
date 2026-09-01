class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for post, pre in prerequisites:
            if pre not in adj:
                adj[pre] = [post]
            else:
                adj[pre].append(post)
        indegree = [0] * numCourses
        for key in adj:
            for val in adj[key]:
                indegree[val] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        topo = []
        while q:
            node = q.pop()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return len(topo) == numCourses
            
            
            


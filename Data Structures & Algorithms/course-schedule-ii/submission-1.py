class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        preMap = {i: [] for i in range(numCourses)}
        cycle = set()

        for course, pre in prerequisites:
            preMap[course].append(pre)
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            res.append(course)
            cycle.remove(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
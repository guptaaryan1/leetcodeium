class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        cycle = set()
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)
        def dfs(course):
            print(f"recurse for course {course}")
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
            
            
        return res
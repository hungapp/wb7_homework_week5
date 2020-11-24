# bfs using topological sort, if the length of the result list doesn't equal to the number of courses then there's a circle in the graph
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1
        
        bfs = [i for i in range(numCourses) if in_degree[i] == 0]
        for i in bfs:
            for j in graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    bfs.append(j)

        return len(bfs) == numCourses

# dfs 
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [False] * numCourses
        
        def dfs(course):
            if visited[course]:
                return False
            else:
                visited[course] = True
            
            for c in graph[course]:
                if not dfs(c):
                    return False
            
            # remember to backtrack
            visited[course] = False
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

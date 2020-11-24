from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = {i:0 for i in range(numCourses)}
        outDegree = {i:[] for i in range(numCourses)}
        
        for prereq in prerequisites:
            parent, child = prereq[1], prereq[0]
            outDegree[parent].append(child)
            inDegree[child] += 1
            
        sources = deque()
        for node in inDegree:
            if inDegree[node] == 0:
                sources.append(node)
        
        courseOrder = []
        while sources:
            node = sources.popleft()
            courseOrder.append(node)
            for child in outDegree[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(courseOrder) != numCourses:
            return []
        
        return courseOrder

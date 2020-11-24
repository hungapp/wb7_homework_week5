class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                stack = [node]
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = color[node] ^ 1
                            stack.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True

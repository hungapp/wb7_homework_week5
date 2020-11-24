class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        cache = [[0] * cols for _ in range(rows)]
        
        def dfs(i, j, cache):
            dy = [0, 0, -1, 1]
            dx = [-1, 1, 0, 0]
            if cache[i][j] != 0:
                return cache[i][j]

            for d in zip(dy, dx):
                y, x = i + d[0], j + d[1]
                if 0 <= y < rows and 0 <= x < cols and matrix[y][x] > matrix[i][j]:
                    cache[i][j] = max(cache[i][j], dfs(y, x, cache))
            cache[i][j] += 1
            return cache[i][j]
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j, cache))
                
        print(cache)
        return ans

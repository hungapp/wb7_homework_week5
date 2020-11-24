class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def get_perimeter(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols: #if boundary
                return 1
            if grid[i][j] == 0: #if empty cell/water
                return 1
            if grid[i][j] == -1: #if island
                return 0
            dy = [0, 0, -1, 1]
            dx = [-1, 1, 0, 0]
            count = 0
            grid[i][j] = -1
            for y, x in zip(dy, dx):
                count += get_perimeter(i + y, j + x)
            return count
        
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans += get_perimeter(i, j)
        return ans            
        

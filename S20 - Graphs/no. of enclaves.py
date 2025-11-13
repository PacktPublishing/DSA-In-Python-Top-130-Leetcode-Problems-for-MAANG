class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            self.dfsCore(i, 0, grid)
            self.dfsCore(i, n - 1, grid)
        
        for i in range(n):
            self.dfsCore(0, i, grid)
            self.dfsCore(m - 1, i, grid)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    count += 1
        
        return count
    
    def dfsCore(self, row, col, grid):
        if (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1):
            grid[row][col] = 0
            self.dfsCore(row - 1, col, grid)
            self.dfsCore(row + 1, col, grid)
            self.dfsCore(row, col - 1, grid)
            self.dfsCore(row, col + 1, grid)
    
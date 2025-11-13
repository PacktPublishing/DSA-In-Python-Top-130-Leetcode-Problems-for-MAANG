class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        count = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if (grid[row][col] == '1'):
                    count += 1
                    self.dfs(row, col)
        return count

    def dfs(self, row, col):
        if (self.isValid(row, col)):
            self.grid[row][col] = '2'
            self.dfs(row - 1, col)
            self.dfs(row + 1, col)
            self.dfs(row, col - 1)
            self.dfs(row, col + 1)

    def isValid(self, row, col):
        if (row < 0 or row >= len(self.grid)):
            return False
        if (col < 0 or col >= len(self.grid[0])):
            return False

        if self.grid[row][col] == '1':
            return True
        return False

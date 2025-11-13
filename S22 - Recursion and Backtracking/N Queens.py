class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append('.')
            self.board.append(row)
        self.solutions = []
        self.backtrack(0)
        return self.solutions
    
    def backtrack(self, row):
        if (row == len(self.board)):
            solution = []
            for row in self.board:
                solution.append(''.join(row))
            self.solutions.append(solution)
        else:
            for i in range(len(self.board[0])):
                if (self.isSafe(self.board, row, i)):
                    self.board[row][i] = 'Q'
                    self.backtrack(row + 1)
                    self.board[row][i] = '.'
        
    def isSafe(self, board, row, col):
        for i in range(len(board)):
            if (board[i][col] == 'Q'):
                return False
        
        i = row - 1
        j = col - 1
        while (i >= 0 and j >= 0):
            if (board[i][j] == 'Q'):
                return False
            i -= 1
            j -= 1
        
        i = row - 1
        j = col + 1
        while (i >= 0 and j < len(board[0])):
            if (board[i][j] == 'Q'):
                return False
            i -= 1
            j += 1
        
        return True
        

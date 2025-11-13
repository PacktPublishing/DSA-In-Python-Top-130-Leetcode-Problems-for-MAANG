class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'O'):
                    board[i][j] = 'U'
        for j in range(n):
            self.dfsCore(0, j, board)
            self.dfsCore(m - 1, j, board)
        for i in range(m):
            self.dfsCore(i, 0, board)
            self.dfsCore(i, n - 1, board)
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'U'):
                    board[i][j] = 'X'
    def dfsCore(self, row, col, board):
        if (row >= 0 and row < len(board) and col >=0 and col < len(board[0]) and board[row][col] == 'U'):
            board[row][col] = 'O'
            self.dfsCore(row - 1, col, board)
            self.dfsCore(row + 1, col, board)
            self.dfsCore(row, col - 1, board)
            self.dfsCore(row, col + 1, board)


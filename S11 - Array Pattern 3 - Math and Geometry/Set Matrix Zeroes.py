class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRow = False
        firstCol = False

        m = len(matrix)
        n = len(matrix[0])

        # Check if first row has zeros
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
                break

        # Check if first column has zeros
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
                break

        # Mark zeros in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set rows and columns to zeros based on marked cells
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row to zeros
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0

        # Set first column to zeros
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0
        

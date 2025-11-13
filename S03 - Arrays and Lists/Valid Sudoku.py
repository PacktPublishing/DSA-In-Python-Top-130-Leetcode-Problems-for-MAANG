class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        gridSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue

                gridNo = (i // 3) * 3 + (j // 3)
                isPresentInRow = value in rowSet[i]
                isPresentInCol = value in colSet[j]
                isPresentInGrid = value in gridSet[gridNo]

                if isPresentInRow or isPresentInCol or isPresentInGrid:
                    return False

                rowSet[i].add(value)
                colSet[j].add(value)
                gridSet[gridNo].add(value)

        return True

        

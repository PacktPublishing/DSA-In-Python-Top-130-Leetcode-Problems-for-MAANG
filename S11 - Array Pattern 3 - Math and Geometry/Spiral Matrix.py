class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        output = []
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        direction = 0
        
        while top <= bottom and left <= right:
            if (direction == 0):
                for j in range(left, right + 1):
                    output.append(matrix[top][j])
                top += 1
                direction = 1
            elif (direction == 1):
                for i in range(top, bottom + 1):
                    output.append(matrix[i][right])
                right -= 1
                direction = 2
            elif (direction == 2):
                for j in range(right, left - 1, -1):
                    output.append(matrix[bottom][j])
                bottom -= 1
                direction = 3
            else:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
                direction = 0
        return output
                    
                

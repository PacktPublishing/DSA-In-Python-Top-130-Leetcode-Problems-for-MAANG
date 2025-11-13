class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        distance =  []
        for i in range(m):
            val = []
            for j in range(n):
                val.append(0)
            distance.append(val)
        
        que = deque()
        for i in range(m):
            for j in range(n):
                if (mat[i][j] == 1):
                    distance[i][j] = m*n
                else:
                    distance[i][j] = 0
                    que.append((i, j))
        
        while (len(que) > 0):
            top = que.popleft()
            row = top[0]
            col = top[1]
            
            newDistance = distance[row][col] + 1
            if (self.isValid(row - 1, col, mat) and distance[row - 1][col] > newDistance):
                distance[row-1][col] = newDistance
                que.append((row - 1, col))
            if (self.isValid(row + 1, col, mat) and distance[row + 1][col] > newDistance):
                distance[row + 1][col] = newDistance
                que.append((row + 1, col))
            
            if (self.isValid(row, col - 1, mat) and distance[row][col - 1] > newDistance):
                distance[row][col - 1] = newDistance
                que.append((row, col - 1))
            
            if (self.isValid(row, col + 1, mat) and distance[row][col + 1] > newDistance):
                distance[row][col + 1] = newDistance
                que.append((row, col + 1))
            
        return distance
    
    def isValid(self, row, col, mat):
        m = len(mat)
        n = len(mat[0])
        if (row < 0 or row >= m or col < 0 or col >= n):
            return False
        if (mat[row][col] != 1):
            return False
        return True
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        start = 1
        end = position[-1] - position[0]
        ans = 1
        
        while (start <= end):
            mid = (start + end)//2
            if (self.isDistancePossible(position, m, mid)):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return ans
    
    def isDistancePossible(self, position, m, dist):
        noOfBallsPlaced = 1
        lastPosition = position[0]
        
        for i in range(1, len(position)):
            if (position[i] >= lastPosition + dist):
                noOfBallsPlaced += 1
                lastPosition = position[i]
        
        if (noOfBallsPlaced < m):
            return False
        else:
            return True
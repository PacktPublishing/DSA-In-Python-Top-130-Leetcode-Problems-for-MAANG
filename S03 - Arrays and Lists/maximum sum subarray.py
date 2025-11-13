class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        currentSum = nums[0]
        
        for i in range(1, len(nums)):
            if (currentSum < 0):
                currentSum = 0
            currentSum += nums[i]
            if (currentSum > maxSoFar):
                maxSoFar = currentSum
                
        return maxSoFar
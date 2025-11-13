class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(0, len(nums) + 1):
            x = x^i
    
        y = 0
        for i in range(0, len(nums)):
            y = y^nums[i];
            
        return x^y
        

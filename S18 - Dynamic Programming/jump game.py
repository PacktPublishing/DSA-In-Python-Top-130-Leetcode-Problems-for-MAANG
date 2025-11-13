class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = nums[0]
        i = 1
        while (i < len(nums) and maxReachable >= i):
            if (i + nums[i] > maxReachable):
                maxReachable = i + nums[i]
            i += 1
            
        if (maxReachable >= len(nums) - 1):
            return True
        else:
            return False
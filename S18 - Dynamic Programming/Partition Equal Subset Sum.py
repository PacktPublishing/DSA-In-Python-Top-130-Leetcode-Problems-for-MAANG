class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2
        dp = [[-1] * (target + 1) for _ in range(len(nums))]
        return self.partition(nums, 0, target, dp)
    
    def partition(self, nums: List[int], index: int, target: int, dp: List[List[int]]) -> bool:
        if target < 0:
            return False
        elif index == len(nums):
            return target == 0
        else:
            if dp[index][target] != -1:
                return dp[index][target]
            else:
                result = self.partition(nums, index + 1, target - nums[index], dp) or \
                         self.partition(nums, index + 1, target, dp)
                dp[index][target] = result
                return result

        

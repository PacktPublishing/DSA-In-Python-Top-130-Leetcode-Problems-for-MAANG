class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)
        return [left, right]
    
    
    def findLeft(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1
        
        while start <= end:
            mid = (start + end)//2
            if (nums[mid] < target):
                start = mid + 1
            elif (nums[mid] > target):
                end = mid - 1
            else:
                ans = mid
                end = mid - 1
        return ans
    
    def findRight(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1
        
        while start <= end:
            mid = (start + end)//2
            if (nums[mid] < target):
                start = mid + 1
            elif (nums[mid] > target):
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans
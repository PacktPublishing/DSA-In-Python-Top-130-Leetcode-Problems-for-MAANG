class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        
        ans = 1
        while (start <= end):
            mid = (start + end)//2
            
            count = 0
            for num in nums:
                if (num <= mid):
                    count += 1
            
            if (count <= mid):
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        
        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        
        ans = 0
        
        for num in nums:
            if (num - 1 not in nSet):
                current = num
                currentStreak = 1
                
                while current + 1 in nSet:
                    currentStreak += 1
                    current += 1
                
                if (currentStreak > ans):
                    ans = currentStreak
        
        return ans

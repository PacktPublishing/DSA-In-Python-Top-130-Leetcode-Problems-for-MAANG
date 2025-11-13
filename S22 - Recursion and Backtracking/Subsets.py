class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.subset = []
        self.subsets = []
        
        self.backtrack(0)
        
        return self.subsets
    
    def backtrack(self, i):
        if (i == len(self.nums)):
            ans = []
            for num in self.subset:
                ans.append(num)
            self.subsets.append(ans)
        else:
            self.backtrack(i + 1)
            
            self.subset.append(self.nums[i])
            self.backtrack(i + 1)
            self.subset.pop()
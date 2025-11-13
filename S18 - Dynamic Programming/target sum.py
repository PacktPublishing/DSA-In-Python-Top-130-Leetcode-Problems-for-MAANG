class Solution:
    def f(self, i, ct):
        if (i < len(self.nums) - 1):
            key = (i, ct)
            if (key in self.ht):
                return self.ht[key]
            self.ht[key] = self.f(i + 1, ct - self.nums[i]) + self.f(i + 1, ct + self.nums[i])
            return self.ht[key]
        else:
            if (ct == 0 and self.nums[i] == 0):
                return 2
            elif (abs(ct) == abs(self.nums[i])):
                return 1
            else:
                return 0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.ht = { }
        return self.f(0, target)

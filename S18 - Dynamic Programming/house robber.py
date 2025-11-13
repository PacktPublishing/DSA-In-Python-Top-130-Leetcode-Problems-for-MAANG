class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = { }
        self.nums = nums
        return self.f(0, True)
    def f(self, i, canRob):
        if (i == len(self.nums) - 1):
            if (canRob == True):
                return self.nums[i]
            else:
                return 0
        else:
            if ((i, canRob) not in self.dp):
                if (canRob == True):
                    self.dp[(i, canRob)] = max(self.nums[i] + self.f(i + 1, False),
                                         self.f(i + 1, True))
                else:
                    self.dp[(i, canRob)] = self.f(i + 1, True)
            return self.dp[(i, canRob)]}

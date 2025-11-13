class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        n = len(nums)
        ans = [-1]*n
        
        
        for i in range(1, n):
            current = nums[i]
            while (len(stack) > 0 and nums[stack[-1]] < current):
                ans[stack[-1]] = current
                stack.pop()
            stack.append(i)
        
        
        for i in range(0, n):
            current = nums[i]
            while (len(stack) > 0 and nums[stack[-1]] < current):
                ans[stack[-1]] = current
                stack.pop()
        
        return ans
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        n = len(nums)
        for i in range(1, n):
            left.append(left[i-1]*nums[i-1])
        
        right = [1]*(n+1)
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        output = []
        for i in range(n):
            output.append(left[i]*right[i])
        return output

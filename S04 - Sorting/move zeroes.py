class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[i], nums[start] = nums[start], nums[i]
                start = start + 1}

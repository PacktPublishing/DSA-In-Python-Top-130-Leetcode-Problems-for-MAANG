class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        n = len(nums)
        nums.sort()
        ans = []
        while (i < n):
            if (i == 0 or (i - 1 >= 0 and nums[i] != nums[i-1])):
                firstElement = nums[i]
                target = 0 - firstElement
                pairs = self.twoSum(nums, i + 1, n - 1, target)
                for pair in pairs:
                    triplet = [firstElement, pair[0], pair[1]]
                    ans.append(triplet)
            i += 1
        
        return ans
    def twoSum(self, nums, start, end, target):
        f = start
        s = end
        pairs = []
        while (f < s):
            if (f - 1 >= start and nums[f-1] == nums[f]):
                f = f + 1
                continue
            if (s + 1 <= end and nums[s+1] == nums[s]):
                s = s - 1
                continue
            if (nums[f] + nums[s] < target):
                f += 1
            elif (nums[f] + nums[s] > target):
                s -= 1
            else:
                pair = [nums[f], nums[s]]
                pairs.append(pair)
                f += 1
        return pairs
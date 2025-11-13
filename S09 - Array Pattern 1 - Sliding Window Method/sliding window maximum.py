class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answers = []
        n = len(nums)
        de = Deque()
        de.append(0)
        for i in range(1, k):
            while (len(de) > 0 and nums[de[-1]] < nums[i]):
                de.pop()
            de.append(i)
        answers.append(nums[de[0]])
        
        for j in range(k, n):
            startingPoint = j - k + 1
            while (len(de) > 0 and de[0] < startingPoint):
                de.popleft()
            
            while (len(de) > 0 and nums[de[-1]] < nums[j]):
                de.pop()
            
            de.append(j)
            answers.append(nums[de[0]])
        
        return answers
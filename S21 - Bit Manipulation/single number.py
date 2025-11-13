class Solution(object):
    def singleNumber(self, nums):
      list=[]
      for i in range(0,len(nums)):
        if nums[i] in list:
         list.remove(nums[i])
        else:
         list.append(nums[i])
      return list[0]
class Solution(object):
 def twoSum(self,numbers, target):
  final=[]
  low,high=0,len(numbers)-1
  while low < high:

   nums=numbers[low] + numbers[high]
   if nums == target:
    return [low+1,high+1]
   elif nums>target:
    high=high-1
   else:
    low=low+1

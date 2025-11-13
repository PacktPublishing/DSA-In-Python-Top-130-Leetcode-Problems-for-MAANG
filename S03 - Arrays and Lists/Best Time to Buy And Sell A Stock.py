class Solution(object):
    def maxProfit(self, prices):
      result=0
      maxValue=prices[0]
      minValue=0
#   print("Hello from a function")
      for i in range(1,len(prices)):
       if maxValue>prices[i]:
        maxValue=prices[i]
       else:
        minValue=prices[i]-maxValue
        if minValue>result:
         result=minValue
      return result
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = end
        while (start <= end):
            mid = (start + end)//2
            if (self.countHours(piles, mid) > h):
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        return ans
    def countHours(self, piles, speed):
        noOfHours = 0
        for pile in piles:
            noOfHours += math.ceil(pile/speed)
        return noOfHours

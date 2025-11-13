class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(0, 32):
            if (n & (1 << i) != 0):
                count += 1
        return count

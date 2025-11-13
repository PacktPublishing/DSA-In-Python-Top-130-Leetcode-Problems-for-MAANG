class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.f(n)

    def f(self, i):
        if (i <= 1):
            return 0
        elif (i%2 == 0):
            return 1 + self.f(i/2)
        else:
            return 1 + min(self.f(i + 1), self.f(i - 1))


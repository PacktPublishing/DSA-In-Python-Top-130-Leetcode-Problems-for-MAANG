class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = { }
        self.coins = coins
        return self.f(amount)
        
    def f(self, i):
        if (i <= 0):
            return 0
        else:
            ans = -1
            if (i in self.dp):
                return self.dp[i]
            else:
                for coin in self.coins:
                    if (coin <= i):
                        val = self.f(i - coin)
                        if (val != -1 and (ans == -1 or val + 1 < ans)):
                            ans = val + 1
                self.dp[i] = ans
                return ans
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            oneDigit = int(s[i-1:i])
            twoDigit = int(s[i-2:i])
            
            if (oneDigit >= 1 and oneDigit <= 9):
                dp[i] += dp[i-1]
            
            if (twoDigit >= 10 and twoDigit <= 26):
                dp[i] += dp[i-2]
            
        return dp[n]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = s[i:i + 2]

        for size in range(3, n + 1):
            for i in range(n - size + 1):
                start = i
                end = i + size - 1
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1]
                    if dp[start][end]:
                        ans = s[start:end + 1]

        return ans
        

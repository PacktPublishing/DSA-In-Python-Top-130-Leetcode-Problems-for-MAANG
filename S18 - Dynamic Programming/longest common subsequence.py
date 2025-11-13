class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = { }
        self.text1 = text1
        self.text2 = text2
        n = len(text1)
        m = len(text2)
        return self.lcs(n - 1, m - 1)
    def lcs(self, i, j):
        if (i == -1 or j == -1):
            return 0
        else:
            if ((i, j) not in self.dp):
                if (self.text1[i] == self.text2[j]):
                    self.dp[(i, j)] = self.lcs(i - 1, j - 1) + 1
                else:
                    self.dp[(i, j)] = max(self.lcs(i-1, j), self.lcs(i, j-1))
            return self.dp[(i, j)]}

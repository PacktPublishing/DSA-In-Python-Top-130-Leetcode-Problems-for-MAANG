class Solution:
    def addToDict(self, ht, ch):
        if (ch not in ht):
            ht[ch] = 1
        else:
            ht[ch] += 1
        
    def removeFromDict(self, ht, ch):
        ht[ch] -= 1
    
    def isValid(self, ht):
        for ch in ht:
            if (ht[ch] > 1):
                return False
        return True
    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        fp = 0
        sp = 0
        ht = { }
        ans = 0
        while (sp < n):
            self.addToDict(ht, s[sp])
            while (fp < sp and not self.isValid(ht)):
                self.removeFromDict(ht, s[fp])
                fp += 1
            
            length = sp - fp + 1
            ans = max(ans, length)
            sp += 1
        
        return ans
            
    
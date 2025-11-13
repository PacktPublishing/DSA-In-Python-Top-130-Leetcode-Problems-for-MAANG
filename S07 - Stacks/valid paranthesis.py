class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if (self.isOpening(ch)):
                st.append(ch)
            else:
                if (len(st) == 0):
                    return False
                else:
                    if (self.doesMatch(st[-1], ch)):
                        st.pop()
                    else:
                        return False
        if (len(st) == 0):
            return True
        else:
            return False
    def isOpening(self, ch):
        return ch == '(' or ch == '\{' or ch == '['
    def doesMatch(self, och, cch):
        return (och == '(' and cch == ')') or (och == '\{' and cch == '\}') or (och == '[' and cch == ']')

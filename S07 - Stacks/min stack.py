class MinStack:
    def __init__(self):
        self.a = []
        self.b = []
    def push(self, val: int) -> None:
        self.a.append(val)
        if (len(self.b) == 0 or val <= self.b[-1]):
            self.b.append(val)
    def pop(self) -> None:
        if (len(self.a) > 0):
            if (self.a[-1] == self.b[-1]):
                self.b.pop()
            self.a.pop()
    def top(self) -> int:
        return self.a[-1]
    def getMin(self) -> int:
        return self.b[-1]

# Your MinStack object will be instantiated and called as such:\
# obj = MinStack()\
# obj.push(val)\
# obj.pop()\
# param_3 = obj.top()\
# param_4 = obj.getMin()}

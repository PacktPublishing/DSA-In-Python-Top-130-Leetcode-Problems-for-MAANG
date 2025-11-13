class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answers = []
        self.f(0, target, [], candidates)
        return self.answers
    
    def f(self, i, rem, combination, candidates):
        if (i == len(candidates)):
            if (rem == 0):
                combi = []
                for num in combination:
                    combi.append(num)
                self.answers.append(combi)
        else:
            maxTimes = rem//candidates[i]
            for k in range(0, maxTimes + 1):
                newTarget = rem
                for j in range(k):
                    combination.append(candidates[i])
                    newTarget -= candidates[i]
                self.f(i + 1, newTarget, combination, candidates)
                for j in range(k):
                    combination.pop()
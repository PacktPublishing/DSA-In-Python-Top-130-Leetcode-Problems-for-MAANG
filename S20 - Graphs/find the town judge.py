class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 : return 1\
        indeg= collections.defaultdict(int)
        outdeg= collections.defaultdict(int)
        print(indeg, outdeg)
        for a,b in trust:
            outdeg[a]+=1
            indeg[b]+=1
        print(indeg, outdeg)
        for key,val in indeg.items():
            if val==n-1 and outdeg[key]==0: return key
        return -1

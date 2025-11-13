class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        result = [[intervals[0][0], intervals[0][1]]]
        for i in range(len(intervals)):
            interval = intervals[i]
            if (interval[0] <= result[-1][1]):
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append([interval[0], interval[1]])
        return result
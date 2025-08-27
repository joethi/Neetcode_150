from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        for i in range(len(intervals)-1):
            for j in range(len(intervals)-i-1):
                if intervals[j][0] > intervals[j+1][0]:
                    temp = intervals[j]
                    intervals[j] = intervals[j+1]
                    intervals[j+1] = temp
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res

intervals = [[1,2],[2,3]]
sol_obj = Solution()
print(sol_obj.merge(intervals))




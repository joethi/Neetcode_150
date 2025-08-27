from typing import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mt_strt = []
        mt_end = []
        for interval in intervals:
            mt_strt.append(interval.start)
            mt_end.append(interval.end)
        mt_strt.sort()
        mt_end.sort()
        # for strt in range(interval):
        l, r = 0, 0
        ct, max_ct = 0, 0
        while l < len(mt_strt):
            if mt_strt[l] < mt_end[r]:
                l += 1
                ct += 1
            else:
                r += 1
                ct -= 1
            max_ct = max(ct,max_ct)
        # while r < len(mt_end):
        #     ct -= 1
        #     r += 1
        #     max_ct = max(ct,max_ct)
        return max_ct

intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
sol_obj = Solution()
sol_obj.minMeetingRooms(intervals)

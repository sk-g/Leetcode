# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        heap = []
        heapq.heappush(heap,intervals[0].end)
        for i in range(1,len(intervals)):
            x = intervals[i]
            if x.start >= heap[0]:
                heapq.heapreplace(heap,x.end)
            else:
                heapq.heappush(heap,x.end)
        return len(heap)
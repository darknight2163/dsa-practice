# Problem: Merge all overlapping intervals and return a list of
#          non-overlapping intervals that cover all the input intervals.
# Approach: First sort intervals by their starting point. Then compare
#           each interval with the current interval. If they overlap,
#           extend the current interval; otherwise, add the current
#           interval to the answer and start a new one.
# Time Complexity: O(n log n) due to sorting.
# Space Complexity: O(n) for the output array.
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        n = len(intervals)

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, n):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                ans.append([start1, end1])
                start1 = start2
                end1 = end2

        ans.append([start1, end1])

        return ans
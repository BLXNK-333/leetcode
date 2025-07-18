"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: (i[0], i[1]))
        result = []
        st, end = intervals[0]

        for x, y in intervals:
            if end >= x:
                end = max(y, end)
            else:
                result.append([st, end])
                st, end = x, y

        if not result or end != result[-1][1]:
            result.append([st, end])

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(sol.merge(intervals=[[1, 4], [4, 5]]))
    print(sol.merge(intervals=[[1, 4], [2, 3]]))

"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum
minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""

from typing import List


class Solution:
    def _time_to_int(self, time: str):
        h, m = map(int, time.split(":"))
        return 60 * int(h) + int(m)

    def _calc_diff(self, t1: int, t2: int):
        return min(t2 - t1, 1440 - t2 + t1)

    def findMinDifference(self, timePoints: List[str]) -> int:
        diff = sorted(self._time_to_int(t) for t in timePoints)
        min_diff = 1440
        diff.append(min_diff + diff[0])

        for i in range(1, len(diff)):
            cur_dif = self._calc_diff(diff[i - 1], diff[i])
            if cur_dif < min_diff:
                min_diff = cur_dif

        return min_diff


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMinDifference(timePoints=["00:00", "23:59", "00:00"]) == 0
    assert sol.findMinDifference(timePoints=["00:00", "23:59"]) == 1
    assert sol.findMinDifference(timePoints=["01:01", "02:01"]) == 60

    assert sol.findMinDifference(timePoints=["19:00", "01:00"]) == 360
    assert sol.findMinDifference(timePoints=["02:39", "10:26", "21:43"]) == 296

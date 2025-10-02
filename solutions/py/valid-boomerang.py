"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y
plane, return true if these points are a boomerang.
A boomerang is a set of three points that are all distinct and not in a
straight line.

Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false

Constraints:
points.length == 3
points[i].length == 2
0 <= xi, yi <= 100
"""

from typing import List
import math
from itertools import chain


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1, x2, y2, x3, y3 = list(chain(*sorted(points)))
        if (x1 == x2 and y1 == y2) or (x2 == x3 and y2 == y3) or (x1 == x3 and y1 == y3):
            return False
        if x1 + y1 < x2 + y2 > x3 + y3:
            return True
        angle1 = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angle2 = math.degrees(math.atan2(y3 - y2, x3 - x2))
        return angle1 != angle2


if __name__ == '__main__':
    sol = Solution()
    assert sol.isBoomerang(points=[[1, 1], [2, 3], [3, 2]]) == True
    assert sol.isBoomerang(points=[[1, 1], [2, 2], [3, 3]]) == False
    assert sol.isBoomerang(points=[[0, 0], [1, 1], [1, 1]]) == False
    assert sol.isBoomerang(points=[[2, 2], [8, 8], [3, 3]]) == False

"""
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c]
represents the number of points at position (r, c) on the matrix. Two robots
are playing a game on this matrix.
Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot
may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1,
c)).
At the start of the game, the first robot moves from (0, 0) to (1, n-1),
collecting all the points from the cells on its path. For all cells (r, c)
traversed on the path, grid[r][c] is set to 0. Then, the second robot moves
from (0, 0) to (1, n-1), collecting the points on its path. Note that their
paths may intersect with one another.
The first robot wants to minimize the number of points collected by the second
robot. In contrast, the second robot wants to maximize the number of points it
collects. If both robots play optimally, return the number of points collected
by the second robot.

Example 1:
Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the
optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.

Example 2:
Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the
optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.

Example 3:
Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the
optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.

Constraints:
grid.length == 2
n == grid[r].length
1 <= n <= 5 * 104
1 <= grid[r][c] <= 105
"""

from typing import List


class Solution:
    def _get_best_points(self, grid: List[List[int]]) -> int:
        S1, S2 = sum(grid[0]), sum(grid[1])
        n = len(grid[0])
        R_sum = 0

        for i in range(n):
            s1 = S1 - grid[0][i]
            if s1 >= S2:
                S1 = s1
                S2 -= grid[1][i]
                R_sum += grid[0][i]
                grid[0][i] = 0
            else:
                R_sum += grid[0][i]
                grid[0][i] = 0
                while i < n:
                    R_sum += grid[1][i]
                    grid[1][i] = 0
                    i += 1
                return R_sum

        last = grid[1][-1]
        grid[1][-1] = 0
        return R_sum + last

    def _make_ruined(self, grid: List[List[int]]):
        n = len(grid[0])
        S1 = sum(grid[0])
        S2 = 0

        for i in range(n):
            s1 = S1 - grid[0][i]
            s2 = S2 + grid[1][i]
            if s1 >= s2:
                S1, S2 = s1, s2
                grid[0][i] = 0
            else:
                grid[0][i] = 0
                while i < n:
                    grid[1][i] = 0
                    i += 1
                return

    def gridGame(self, grid: List[List[int]]) -> int:
        self._make_ruined(grid)
        R2 = self._get_best_points(grid)
        return R2


if __name__ == '__main__':
    sol = Solution()
    assert sol.gridGame(grid=[[2, 5, 4], [1, 5, 1]]) == 4
    assert sol.gridGame(grid=[[3, 3, 1], [8, 5, 2]]) == 4
    assert sol.gridGame(grid=[[20, 3, 20, 17, 2, 12, 15, 17, 4, 15],
                              [20, 10, 13, 14, 15, 5, 2, 3, 14, 3]]) == 63

"""
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has
one of two values:
0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper
left corner (0, 0) to the lower right corner (m - 1, n - 1).

Example 1:
Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path
from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles,
so we return 0.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""

import heapq
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        inf = 10 ** 6
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        costs = [[inf] * m for _ in range(n)]
        costs[0][0] = 0
        heap = [(0, 0, 0)]

        while costs[-1][-1] == inf:
            cur_cost, ni, nj = heapq.heappop(heap)
            for di, dj in directions:
                nx = ni + di
                ny = nj + dj
                if 0 <= nx < n and 0 <= ny < m:
                    next_cost = cur_cost + grid[nx][ny]
                    if next_cost < costs[nx][ny]:
                        costs[nx][ny] = next_cost
                        heapq.heappush(heap, (next_cost, nx, ny))

        return costs[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.minimumObstacles(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]) == 2
    assert sol.minimumObstacles(grid=[[0], [0]]) == 0
    assert sol.minimumObstacles(
        grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]) == 0

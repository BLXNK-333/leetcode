"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        DP = [[0] * m for _ in range(n)]
        DP[0][0] = grid[0][0]

        for i in range(1, n):
            DP[i][0] = DP[i - 1][0] + grid[i][0]

        for j in range(1, m):
            DP[0][j] = DP[0][j - 1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + grid[i][j]

        return DP[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c)
represents:
A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations
any number of times:
Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his
starting cell optimally, or 0 if no water cell exists.
An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c -
1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move
to cell (2,3) and collect 4 fish.

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single
fish.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
"""

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i: int, j: int):
            if i == n or j == m or i < 0 or j < 0 or not grid[i][j]:
                return 0

            S = grid[i][j]
            grid[i][j] = 0

            S += dfs(i + 1, j)
            S += dfs(i - 1, j)
            S += dfs(i, j + 1)
            S += dfs(i, j - 1)

            return S

        max_fishes = 0
        for ni in range(n):
            for nj in range(m):
                max_fishes = max(max_fishes, dfs(ni, nj))

        return max_fishes


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxFish(grid=[[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
    print(sol.findMaxFish(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))

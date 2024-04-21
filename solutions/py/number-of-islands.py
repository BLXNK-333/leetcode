"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        counter = 0
        n, m = len(grid), len(grid[0])
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(row, col):
            visited.add((row, col))
            for di, dj in direction:
                x, y = row + di, col + dj
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited and grid[x][y] == "1":
                    dfs(x, y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    counter += 1
        return counter


if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]))

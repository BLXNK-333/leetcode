"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and
grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around
the island. One cell is a square with side length 1. The grid is rectangular, width and height
don't exceed 100. Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""

from typing import List


class Solution:
    def find_the_edge(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return i, j

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        counter = 0
        n, m = len(grid), len(grid[0])
        visited = set()
        queue = set()
        queue.add(self.find_the_edge(grid))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            i, j = queue.pop()
            visited.add((i, j))
            for di, dj in directions:
                x, y = i + di, j + dj
                if 0 > x or x == n or 0 > y or y == m or not grid[x][y]:
                    counter += 1
                elif (x, y) not in visited:
                    queue.add((x, y))
        return counter


if __name__ == '__main__':
    sol = Solution()
    assert sol.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    print(sol.islandPerimeter([[1, 1], [1, 1]]))

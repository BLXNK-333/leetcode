"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of
a '/', '\', or blank space ' '. These characters divide the square into
contiguous regions.
Given the grid grid represented as a string array, return the number of
regions.
Note that backslash characters are escaped, so a '\' is represented as '\\'.

Example 1:
Input: grid = [" /","/ "]
Output: 2

Example 2:
Input: grid = [" /","  "]
Output: 1

Example 3:
Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/,
and "/\\" refers to /\.

Constraints:
n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
"""

from typing import List


class Solution:
    def make_matrix(self, grid: List[str]):
        n = len(grid) * 3
        mtrx = [[0] * n for _ in range(n)]

        gi = gj = 0
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                if grid[gi][gj] == "\\":
                    mtrx[i][j] = 1
                    mtrx[i + 1][j + 1] = 1
                    mtrx[i + 2][j + 2] = 1
                elif grid[gi][gj] == "/":
                    mtrx[i + 2][j] = 1
                    mtrx[i + 1][j + 1] = 1
                    mtrx[i][j + 2] = 1

                gj += 1

            gi += 1
            gj = 0
        return mtrx

    def regionsBySlashes(self, grid: List[str]) -> int:
        mtrx = self.make_matrix(grid)
        n, counter = len(mtrx), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(n):
                if not mtrx[i][j]:
                    queue = {(i, j)}

                    while queue:
                        x, y = next(iter(queue))
                        mtrx[x][y] = 1
                        queue.discard((x, y))
                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < n and 0 <= ny < n and not mtrx[nx][ny]:
                                queue.add((nx, ny))

                    counter += 1
        return counter


if __name__ == '__main__':
    sol = Solution()
    print(sol.regionsBySlashes(["/\\", "\\/"]))

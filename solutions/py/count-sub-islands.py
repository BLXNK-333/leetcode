"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's
(representing water) and 1's (representing land). An island is a group of 1's
connected 4-directionally (horizontal or vertical). Any cells outside of the
grid are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1
that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.

Example 1:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid
on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island.
There are three sub-islands.

Example 2:
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid
on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island.
There are two sub-islands.

Constraints:
m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""

from typing import List


class Solution:
    def __init__(self):
        self._directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        cnt = 0
        n, m = len(grid1), len(grid1[0])

        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    queue = [(i, j)]
                    inside = 1

                    while queue:
                        x, y = queue.pop()
                        grid2[x][y] = -1
                        if grid1[x][y] != 1:
                            inside = 0

                        for dx, dy in self._directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and grid2[nx][ny] == 1:
                                queue.append((nx, ny))

                    cnt += inside
        return cnt


if __name__ == '__main__':
    sol = Solution()
    assert sol.countSubIslands(
        grid1=[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0],
               [1, 1, 0, 1, 1]],
        grid2=[[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0],
               [0, 1, 0, 1, 0]]
    ) == 3
    
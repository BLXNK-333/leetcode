"""
You are given an n x n binary matrix grid where 1 represents land and 0
represents water.
An island is a 4-directionally connected group of 1's not connected to any
other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""

from typing import List, Tuple
from collections import deque


class Solution:
    def __init__(self):
        self._directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def find_island(self, grid: List[List[int]]) -> List[Tuple[int, int]]:
        """
        It's returns all first island's coordinates.
        """
        n, m = len(grid), len(grid[0])
        queue = []
        island = []

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    queue.append((i, j))
                    grid[i][j] = 2
                    while queue:
                        i, j = queue.pop()
                        island.append((i, j))
                        for di, dj in self._directions:
                            x = i + di
                            y = j + dj
                            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                                grid[x][y] = 2
                                queue.append((x, y))

                    return island
        return []

    def find_min_distance(
            self,
            grid: List[List[int]],
            island: List[Tuple[int, int]]
    ) -> int:
        """
        It's finds minimum distance between islands.
        """
        distance = 0
        queue = deque(island)
        n, m = len(grid), len(grid[0])

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in self._directions:
                    x, y = i + di, j + dj
                    if 0 <= x < n and 0 <= y < m:
                        if grid[x][y] == 1:
                            return distance
                        elif not grid[x][y]:
                            grid[x][y] = -1
                            queue.append((x, y))
            distance += 1
        return -1

    def shortestBridge(self, grid: List[List[int]]) -> int:
        island = self.find_island(grid)
        return self.find_min_distance(grid, island)


if __name__ == '__main__':
    sol = Solution()
    assert sol.shortestBridge([[0, 1], [1, 0]]) == 1
    assert sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
    assert sol.shortestBridge([
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]) == 1

    assert sol.shortestBridge([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0]
    ]) == 2

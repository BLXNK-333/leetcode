"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k
times.
In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""

from typing import List
from itertools import chain, batched


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        shift = k % (m * n)

        array_grid = list(chain.from_iterable(grid))
        array_grid = array_grid[-shift:] + array_grid[:-shift]
        return list(map(list, batched(array_grid, n)))




if __name__ == '__main__':
    sol = Solution()

    assert sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1) == [[9,1,2],[3,4,5],[6,7,8]]
    assert sol.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4) == \
            [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    assert sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9) == [[1,2,3],[4,5,6],[7,8,9]]
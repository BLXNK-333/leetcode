"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
Follow up: Could you find an O(n + m) solution?
"""

from typing import List


class Solution:
    def bs(self, array: list) -> int:
        L, R = -1, len(array)
        while L + 1 < R:
            M = (L + R) // 2
            if array[M] < 0:
                R = M
            else:
                L = M
        return R

    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for array in grid:
            counter += len(array) - self.bs(array)
        return counter


if __name__ == "__main__":
    sol = Solution()
    print(sol.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
    print(sol.countNegatives([[3, 2], [1, 0]]))

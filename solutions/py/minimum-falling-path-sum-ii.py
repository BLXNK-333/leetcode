"""
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero
shifts.
A falling path with non-zero shifts is a choice of exactly one element from each row of grid
such that no two elements chosen in adjacent rows are in the same column.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation:
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:
Input: grid = [[7]]
Output: 7

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""

from typing import List


class Solution:
    def get_two_min(self, row: List[int]) -> tuple:
        a = b = float("inf")
        i = j = -1
        for idx, number in enumerate(row):
            if number < a:
                b = a
                j = i
                a = number
                i = idx
            elif number < b:
                b = number
                j = idx
        if j == -1:
            j = i
        return (a, i), (b, j)

    def get_valid_min(self, cur_i: int, minimums: tuple):
        if cur_i != minimums[0][1]:
            return minimums[0][0]
        else:
            return minimums[1][0]

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n == 1:
            return min(grid[0])

        dp = grid[0]
        for i in range(1, n):
            new_dp = []
            minimums = self.get_two_min(dp)
            for j in range(m):
                valid_min = self.get_valid_min(j, minimums)
                new_dp.append(valid_min + grid[i][j])

            dp = new_dp
        return min(dp)


if __name__ == '__main__':
    sol = Solution()
    assert sol.minFallingPathSum(
        grid=[[-37, 51, -36, 34, -22], [82, 4, 30, 14, 38], [-68, -52, -92, 65, -85], [-49, -3, -77, 8, -19],
              [-60, -71, -21, -62, -73]]) == -268

    assert sol.minFallingPathSum(
        [[50, -18, -38, 39, -20, -37, -61, 72, 22, 79], [82, 26, 30, -96, -1, 28, 87, 94, 34, -89],
         [55, -50, 20, 76, -50, 59, -58, 85, 83, -83], [39, 65, -68, 89, -62, -53, 74, 2, -70, -90],
         [1, 57, -70, 83, -91, -32, -13, 49, -11, 58], [-55, 83, 60, -12, -90, -37, -36, -27, -19, -6],
         [76, -53, 78, 90, 70, 62, -81, -94, -32, -57], [-32, -85, 81, 25, 80, 90, -24, 10, 27, -55],
         [39, 54, 39, 34, -45, 17, -2, -61, -81, 85], [-77, 65, 76, 92, 21, 68, 78, -13, 39, 22]]) == -807

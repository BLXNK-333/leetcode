"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through
matrix.
A falling path starts at any element in the first row and chooses the element in the next row
that is either directly below or diagonally left/right. Specifically, the next element from
position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[-1]
        for i in range(len(matrix) - 2, -1, -1):
            temp = [min(dp[0], dp[1]) + matrix[i][0]]
            for j in range(1, len(matrix[0]) - 1):
                temp.append(min(dp[j - 1], dp[j], dp[j + 1]) + matrix[i][j])
            temp.append(min(dp[-2], dp[-1]) + matrix[i][-1])
            dp = temp
        return min(dp)


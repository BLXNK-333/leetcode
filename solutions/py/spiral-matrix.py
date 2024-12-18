"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        result = []
        length = n * m
        cnt, i, j, di, dj = 0, 0, -1, 0, 1
        visited_field = 1000

        while cnt < length:
            x, y = i + di, j + dj
            if 0 <= x < n and 0 <= y < m and matrix[x][y] != visited_field:
                result.append(matrix[x][y])
                matrix[x][y] = visited_field
                i, j = x, y
                cnt += 1
            else:
                di, dj = dj, -di

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

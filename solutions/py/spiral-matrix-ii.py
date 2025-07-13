"""
Given a positive integer n, generate an n x n matrix filled with elements from
1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mtrx = [[0] * n for _ in range(n)]
        n2 = n * n
        i, j, di, dj, cnt = 0, -1, 0, 1, 1

        while cnt <= n2:
            x, y = i + di, j + dj
            if x < n and y < n and not mtrx[x][y]:
                mtrx[x][y] = cnt
                i, j = x, y
                cnt += 1
            else:
                di, dj = dj, -di

        return mtrx


if __name__ == '__main__':
    sol = Solution()
    print(*sol.generateMatrix(2), sep="\n")


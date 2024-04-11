"""
There is an m x n grid with a ball. The ball is initially at the position [startRow,
startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid
(possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to
the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move
the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0

        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j]:
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n:
                                new_dp[ni][nj] += dp[i][j]
                            else:
                                result += dp[i][j]
                                result %= MOD
            dp = new_dp

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
    print(sol.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))

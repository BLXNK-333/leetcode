"""
There is a robot on an m x n grid. The robot is initially located at the top-
left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.
Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2
* 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the
bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mtrx = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                mtrx[i][j] = mtrx[i - 1][j] + mtrx[i][j - 1]

        return mtrx[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.uniquePaths(m=3, n=7) == 28
    assert sol.uniquePaths(m=51, n=9) == 1916797311

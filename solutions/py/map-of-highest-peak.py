"""
You are given an integer matrix isWater of size m x n that represents a map of
land and water cells.
If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:
The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A
cell is adjacent to another cell if the former is directly north, east, south,
or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is
maximized.
Return an integer matrix height of size m x n where height[i][j] is cell (i,
j)'s height. If there are multiple solutions, return any of them.

Example 1:
Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

Example 2:
Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the
rules will also be accepted.

Constraints:
m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.
Note: This question is the same as 542:
https://leetcode.com/problems/01-matrix/
"""

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        mtrx = [[0] * m for _ in range(n)]

        que = []

        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    que.append((i, j, 0))
                    isWater[i][j] = -1

        while que:
            new_que = []
            for i, j, h in que:
                nh = h + 1
                mtrx[i][j] = h

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and isWater[ni][nj] > -1:
                        new_que.append((ni, nj, nh))
                        isWater[ni][nj] = -1
            que = new_que

        return mtrx


if __name__ == '__main__':
    sol = Solution()
    print(sol.highestPeak(isWater=[[0, 1], [0, 0]]))
    print(sol.highestPeak(isWater=[[0, 0, 1], [1, 0, 0], [0, 0, 0]]))

"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other
words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k
rows, 1 column), where k can be of any size. At least one horizontal or
vertical cell separates between two battleships (i.e., there are no adjacent
battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
Follow up: Could you do it in one-pass, using only O(1) extra memory and
without modifying the values board?
"""

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        visited = set()
        count = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(n):
            for j in range(m):
                if (i, j) in visited:
                    continue

                if board[i][j] == "X":
                    ship = [(i, j)]
                    visited.add((i, j))

                    while ship:
                        cell = ship.pop()
                        x, y = cell
                        for di, dj in dirs:
                            xdi = x + di
                            xdj = y + dj
                            if 0 <= xdi < n and 0 <= xdj < m:
                                if (xdi, xdj) in visited:
                                    continue
                                if board[xdi][xdj] == "X":
                                    ship.append((xdi, xdj))
                                visited.add((xdi, xdj))
                    count += 1
        return count






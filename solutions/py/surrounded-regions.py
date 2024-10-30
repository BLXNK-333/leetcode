"""
You are given an m x n matrix board containing letters 'X' and 'O', capture
regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region
with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input
matrix board.

Example 1:
Input: board =
[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output:
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the
edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

import pprint
from typing import List
from itertools import product


class Solution:
    def _get_around_cells(self, board: List[List[str]], n: int, m: int) -> set:
        around_cells = [(a, b) for a, b in product((0, n - 1), range(m))] + [
            (a, b) for a, b in product(range(n), (0, m - 1))]
        return {(i, j) for i, j in around_cells if board[i][j] == "O"}

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        unchanged = set()
        out_cells = self._get_around_cells(board, n, m)
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while out_cells:
            cur_cell = next(iter(out_cells))
            out_cells.remove(cur_cell)
            if cur_cell in unchanged:
                continue

            unchanged.add(cur_cell)
            i, j = cur_cell

            for di, dj in dirs:
                x = i + di
                y = j + dj
                if (0 <= x < n and 0 <= y < m and board[x][y] == "O"
                        and (x, y) not in unchanged):
                    out_cells.add((x, y))

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in unchanged:
                    board[i][j] = "X"


if __name__ == '__main__':
    mtrx_1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    mtrx_2 = [
        ["X", "O", "X", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "X"],
        ["X", "O", "X", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "X"]
    ]

    sol = Solution()
    sol.solve(mtrx_1)
    pprint.pprint(mtrx_1)

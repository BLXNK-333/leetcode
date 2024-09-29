"""
You are given an 8 x 8 matrix representing a chessboard. There is exactly one
white rook represented by 'R', some number of white bishops 'B', and some
number of black pawns 'p'. Empty squares are represented by '.'.
A rook can move any number of squares horizontally or vertically (up, down,
left, right) until it reaches another piece or the edge of the board. A rook is
attacking a pawn if it can move to the pawn's square in one move.
Note: A rook cannot move through other pieces, such as bishops or pawns. This
means a rook cannot attack a pawn if there is another piece blocking the path.
Return the number of pawns the white rook is attacking.

Example 1:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".",
"."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".","
.",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",
".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example, the rook is attacking all the pawns.

Example 2:
Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."]
,[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","
p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",
".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
The bishops are blocking the rook from attacking any of the pawns.

Example 3:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".",
"."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".","
.",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",
".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
The rook is attacking the pawns at positions b5, d6, and f5.

Constraints:
board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""

from typing import List, Tuple, Optional


class Solution:
    def _get_rook_position(self, board: List) -> Optional[Tuple[int, int]]:
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    return i, j

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = self._get_rook_position(board)
        if not rook_pos:
            return 0

        counter = 0
        i, j = rook_pos
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            x = i + di
            y = j + dj

            while 0 <= x < 8 and 0 <= y < 8 and board[x][y] != "B":
                if board[x][y] == "p":
                    counter += 1
                    break
                x += di
                y += dj

        return counter



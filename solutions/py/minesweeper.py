"""
Let's play the minesweeper game (Wikipedia, online game)!
You are given an m x n char matrix board representing the game board where:
'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above,
below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed
square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc]
represents the next click position among all the unrevealed squares ('M' or
'E').
Return the board after revealing this position according to the following
rules:
If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a
revealed blank 'B' and all of its adjacent unrevealed squares should be
revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change
it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Example 1:
Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E
"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B"
,"B","B","B","B"]]

Example 2:
Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B
"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B"
,"B","B","B","B"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] is either 'M' or 'E'.
"""

from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])
        queue = set()
        queue.add(tuple(click))
        visited = set()
        neighbors = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 1),
                     (1, -1), (1, 0), (1, 1)]

        while queue:
            cur = next(iter(queue))
            queue.remove(cur)
            if cur in visited:
                continue
            visited.add(cur)
            i, j = cur

            if board[i][j] == "M":
                board[i][j] = "X"
                return board

            mines_cnt = 0
            for di, dj in neighbors:
                x = i + di
                y = j + dj

                if 0 <= x < n and 0 <= y < m:
                    if board[x][y] == "M":
                        mines_cnt += 1
            if mines_cnt:
                board[i][j] = str(mines_cnt)
                continue

            board[i][j] = "B"
            for di, dj in neighbors:
                x = i + di
                y = j + dj

                if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                    queue.add((x, y))

        return board


if __name__ == '__main__':
    sol = Solution()

    case_1 = sol.updateBoard(board=[
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"]
    ], click=[3, 0])
    # print(*case_1, sep="\n")

    case_2 = sol.updateBoard([
        ["E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "M"],
        ["E", "E", "M", "E", "E", "E", "E", "E"],
        ["M", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E", "E", "E", "E"],
        ["E", "E", "M", "M", "E", "E", "E", "E"]
    ], [0, 0])
    print(*case_2, sep="\n")


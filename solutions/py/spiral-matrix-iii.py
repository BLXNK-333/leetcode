"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The
northwest corner is at the first row and column in the grid, and the southeast
corner is at the last row and column.
You will walk in a clockwise spiral shape to visit every position in this grid.
Whenever you move outside the grid's boundary, we continue our walk outside the
grid (but may return to the grid boundary later.). Eventually, we reach all
rows * cols spaces of the grid.
Return an array of coordinates representing the positions of the grid in the
order you visited them.

Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3
],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1]
,[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:
1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""

from typing import List


class Solution:
    def spiralMatrixIII(
            self,
            rows: int,
            cols: int,
            rStart: int,
            cStart: int
    ) -> List[List[int]]:

        mapp = {(i, j) for i in range(rows) for j in range(cols)}
        result = []

        i, j, di, dj = rStart, cStart, -1, 0
        len_row = len_col = 1
        cnt = 0

        while mapp:
            if (i, j) in mapp:
                result.append([i, j])
                mapp.remove((i, j))

            cnt += 1
            if di and cnt == len_row or dj and cnt == len_col:
                di, dj = dj, -di
                cnt = 0
                if di:
                    len_row += 1
                else:
                    len_col += 1
                continue

            if di:
                i += di
            else:
                j += dj

        return result


def test_case(obj: Solution, rows, cols, rStart, cStart):
    snake = obj.spiralMatrixIII(rows, cols, rStart, cStart)
    arr = [[0] * cols for _ in range(rows)]

    counter = 1
    for i, j in snake:
        arr[i][j] = counter
        counter += 1

    [print(r) for r in arr]


if __name__ == '__main__':
    sol = Solution()
    test_case(sol, 5, 6, 1, 4)


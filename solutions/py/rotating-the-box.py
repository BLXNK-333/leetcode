"""
You are given an m x n matrix of characters box representing a side-view of a
box. Each cell of the box is one of the following:
A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due
to gravity. Each stone falls down until it lands on an obstacle, another stone,
or the bottom of the box. Gravity does not affect the obstacles' positions, and
the inertia from the box's rotation does not affect the stones' horizontal
positions.
It is guaranteed that each stone in box rests on an obstacle, another stone, or
the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.

Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

Constraints:
m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.
"""

from typing import List


class Solution:
    def movie_to_right(self, row: List[str]):
        i, j, n = 0, -1, len(row)
        while i < n:
            if row[i] == "#" and j < 0:
                j = i
            elif row[i] == "." and j >= 0:
                row[j], row[i] = ".", "#"
                j += 1
            elif row[i] == "*":
                j = -1
            i += 1

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        [self.movie_to_right(row) for row in box]
        rotated_box = [list(r) for r in zip(*box[::-1])]
        return rotated_box


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotateTheBox([["#", ".", "#"]]))

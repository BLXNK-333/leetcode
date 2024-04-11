"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

from itertools import chain


class Solution:
    def get_cols(self, s, k):
        c = 0
        while s > 0:
            s -= 2 * k - 2
            c += k - 1
        return c

    def convert(self, s: str, rows: int) -> str:
        if rows == 1:
            return s

        cols = self.get_cols(len(s), rows)
        matrix = [[""] * cols for _ in range(rows)]
        direction = [(1, 0), (-1, 1)]
        _idx = i = j = counter = 0
        di, dj = direction[_idx]

        while counter < len(s):
            matrix[i][j] = s[counter]
            x = i + di
            if x < 0 or x == rows:
                _idx = (_idx + 1) % 2
                di, dj = direction[_idx]
            i += di
            j += dj
            counter += 1
        return "".join(chain(*(row for row in matrix)))


if __name__ == '__main__':
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"
    assert sol.convert("A", 2) == "A"
    assert sol.convert("ABCDE", 4) == "ABCED"

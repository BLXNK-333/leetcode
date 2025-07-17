"""
Given a string columnTitle that represents the column title as appears in an
Excel sheet, return its corresponding column number.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        x = 0
        for i, lt in enumerate(columnTitle[::-1], 0):
            k = ord(lt.lower()) - 97
            x += (26 ** i * (k + 1))
        return x


if __name__ == '__main__':
    sol = Solution()
    assert sol.titleToNumber("A") == 1
    assert sol.titleToNumber("AB") == 28
    assert sol.titleToNumber("ZY") == 701

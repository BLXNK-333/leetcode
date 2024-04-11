"""
Given two integers left and right that represent the range [left, right], return the bitwise AND
of all numbers in this range, inclusive.

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0

Constraints:
0 <= left <= right <= 231 - 1
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        while left and left < right:
            left = left & (left + 1)
            while left and not left & 1:
                left >>= 1
                right >>= 1
                shift += 1
        return left << shift


if __name__ == '__main__':
    sol = Solution()
    assert sol.rangeBitwiseAnd(5, 7) == 4
    assert sol.rangeBitwiseAnd(1, 2147483647) == 0
    assert sol.rangeBitwiseAnd(0, 0) == 0

"""
Given an integer n, add a dot (".") as the thousands separator and return it in
string format.

Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"

Constraints:
0 <= n <= 231 - 1
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        return ".".join(
            [n[max(0, i - 3) : i] for i in range(len(n), -1, -3)][::-1]).lstrip(".")


if __name__ == '__main__':
    sol = Solution()
    print(sol.thousandSeparator(n=987))
    print(sol.thousandSeparator(n=1234))

"""
Given an integer n, return true if it is possible to represent n as the sum of distinct powers
of three. Otherwise, return false.
An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:
Input: n = 21
Output: false

Constraints:
1 <= n <= 107
"""

class Solution:
    def get_factors(self, n):
        res, x = [], 1
        while x <= n:
            res.append(x)
            x *= 3
        return res

    def checkPowersOfThree(self, n: int) -> bool:
        factors = self.get_factors(n)
        i = len(factors) - 1
        x = 0

        while i >= 0:
            y = x + factors[i]
            if y < n:
                x = y
            if y == n:
                return True
            i -= 1
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkPowersOfThree(27))








"""
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the
product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3
and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 104
"""

class Solution:
    def getSquares(self, n: int):
        sqr = []
        i = 1
        while (x := i * i) <= n:
            sqr.append(x)
            i += 1
        return sqr

    def numSquares(self, n: int) -> int:
        array = self.getSquares(n)
        INF = 10 ** 6
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for k in array:
                x = i - k
                if x >= 0 and dp[x] < dp[i]:
                    dp[i] = dp[x]
            dp[i] += 1
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(192))


"""
You are given a square board of characters. You can move on the board starting at the bottom
right square marked with the character 'S'.
You need to reach the top left square marked with the character 'E'. The rest of the squares are
labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you
can go up, left or up-left (diagonally) only if there is no obstacle there.
Return a list of two integers: the first integer is the maximum sum of numeric characters you
can collect, and the second is the number of such paths that you can take to get that maximum
sum, taken modulo 10^9 + 7.
In case there is no path, return [0, 0].

Example 1:
Input: board = ["E23","2X2","12S"]
Output: [7,1]

Example 2:
Input: board = ["E12","1X1","21S"]
Output: [4,2]

Example 3:
Input: board = ["E11","XXX","11S"]
Output: [0,0]

Constraints:
2 <= board.length == board[i].length <= 100
"""

from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        mod = 10 ** 9 + 7
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        board[0] = '0' + board[0][1:]
        dp[n - 1][n - 1] = [1, 1]

        n -= 1
        for i in range(n - 1, -1, -1):
            if board[i][n] == 'X':
                break
            dp[i][n][0] = dp[i + 1][n][0] + int(board[i][n])
            dp[i][n][1] = dp[i + 1][n][1]

        for i in range(n - 1, -1, -1):
            if board[n][i] == 'X':
                break
            dp[n][i][0] = dp[n][i + 1][0] + int(board[n][i])
            dp[n][i][1] = dp[n][i + 1][1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    continue
                max_score = max(dp[i + 1][j][0], dp[i][j + 1][0], dp[i + 1][j + 1][0])
                cnt_path = [item[1] for item in (dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) if item[0] == max_score]
                if cnt_path:
                    dp[i][j][0] = 0 if not max_score else max_score + int(board[i][j])
                    dp[i][j][1] = sum(cnt_path)

        return [max(0, dp[0][0][0] - 1) % mod, dp[0][0][1] % mod]


if __name__ == '__main__':
    sol = Solution()

    assert sol.pathsWithMaxScore(["E11", "XXX", "11S"]) == [0, 0]
    assert sol.pathsWithMaxScore(["E12", "1X1", "21S"]) == [4, 2]
    assert sol.pathsWithMaxScore(["E23", "2X2", "12S"]) == [7, 1]
    assert sol.pathsWithMaxScore(["EX", "XS"]) == [0, 1]
    assert sol.pathsWithMaxScore(["E1", "1S"]) == [1, 2]
    assert sol.pathsWithMaxScore(["E11345", "X452XX", "3X43X4", "44X312", "23452X", "1342XS"]) == [27, 1]

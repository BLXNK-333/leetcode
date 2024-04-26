"""
Given an m x n grid of characters board and a string word, return true if word exists in the
grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, word_index=0):
            if word_index == len(word):
                return True

            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[word_index]:
                return False

            original_char = board[i][j]
            board[i][j] = '#'

            if (dfs(i + 1, j, word_index + 1) or
                    dfs(i - 1, j, word_index + 1) or
                    dfs(i, j + 1, word_index + 1) or
                    dfs(i, j - 1, word_index + 1)):
                return True

            board[i][j] = original_char
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j):
                    return True

        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
    assert sol.exist([["a", "b"], ["c", "d"]], word="cdba")

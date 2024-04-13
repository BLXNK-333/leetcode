"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and
word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m, _max = len(word1) + 1, len(word2) + 1, 0
        LCS = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if word1[i - 1] != word2[j - 1]:
                    if LCS[i - 1][j] > LCS[i][j - 1]:
                        LCS[i][j] = LCS[i - 1][j]
                    else:
                        LCS[i][j] = LCS[i][j - 1]
                else:
                    LCS[i][j] = LCS[i - 1][j - 1] + 1
                if LCS[i][j] > _max:
                    _max = LCS[i][j]
        return len(word1) + len(word2) - _max * 2


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance(word1="leetcode", word2="etco"))

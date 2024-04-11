"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1

Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters only.
"""

class Solution:
    def minCut(self, s: str) -> int:
        hash_map = {}
        inf = 2001
        dp = [inf] * len(s)
        dp[0] = 0

        for shift in range(2):
            for i in range(shift, len(s)):
                j = i - shift
                while 0 <= j and i < len(s) and s[i] == s[j]:
                    hash_map[i] = hash_map.get(i, []) + [j - 1]
                    i += 1
                    j -= 1
        for i in range(1, len(dp)):
            for j in hash_map[i]:
                if j < 0:
                    dp[i] = 0
                    break
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut("abbabab"))
    print(sol.minCut("a"))
"""
An alphabetical continuous string is a string consisting of consecutive letters in the alphabet.
In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest
alphabetical continuous substring.

Example 1:
Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.

Example 2:
Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.

Constraints:
1 <= s.length <= 105
s consists of only English lowercase letters.
"""

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = i = j = 1
        while i < len(s):
            if ord(s[i - 1]) + 1 == ord(s[i]):
                j += 1
            else:
                if j > max_len:
                    max_len = j
                j = 1
            i += 1
        return max(max_len, j)


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestContinuousSubstring("abacaba") == 2
    assert sol.longestContinuousSubstring("abcde") == 5
    assert sol.longestContinuousSubstring("z") == 1
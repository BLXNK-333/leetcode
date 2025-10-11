"""
Given a string s, return true if the s can be palindrome after deleting at most
one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""


class Solution:
    def _check(self, L, R, s):
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1

            else:
                return self._check(L + 1, R, s) or self._check(L, R - 1, s)

        return True



if __name__ == '__main__':
    sol = Solution()
    assert sol.validPalindrome(s="aba") == True
    assert sol.validPalindrome(s="abca") == True
    assert sol.validPalindrome(s="abc") == False

    assert sol.validPalindrome(
        s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    ) == True

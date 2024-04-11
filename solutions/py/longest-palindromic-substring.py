"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ''
        for key in range(0, 2):
            for j in range(key, len(s)):
                i = j - key
                while s[i] == s[j]:
                    if j - i + 1 > len(max_palindrome):
                        max_palindrome = s[i: j + 1]
                    if i - 1 >= 0 and j + 1 < len(s):
                        i -= 1
                        j += 1
                    else:
                        break
        return max_palindrome


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestPalindrome('gagaabbazza'))

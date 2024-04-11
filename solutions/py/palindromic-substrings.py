"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for shift in range(2):
            for i in range(shift, len(s)):
                j = i - shift
                while 0 <= j and i < len(s) and s[i] == s[j]:
                    counter += 1
                    i += 1
                    j -= 1
        return counter


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings('aaa'))
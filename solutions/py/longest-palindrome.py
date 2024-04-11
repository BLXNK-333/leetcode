"""
Given a string s which consists of lowercase or uppercase letters, return the length of the
longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

class Solution:
    def counter(self, s):
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        return d

    def longestPalindrome(self, s: str) -> int:
        mapp = self.counter(s)
        result = is_odd = 0
        for val in mapp.values():
            if val & 1:
                result += val - 1
                is_odd = 1
            else:
                result += val
        return result + is_odd

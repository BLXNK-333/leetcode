"""
The power of the string is the maximum length of a non-empty substring that
contains only one unique character.
Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 0
        cur_length = 0
        cur_letter = s[0]
        for letter in s:
            if letter != cur_letter:
                if cur_length > max_length:
                    max_length = cur_length
                cur_letter = letter
                cur_length = 0
            cur_length += 1
        if cur_length > max_length:
            return cur_length
        return max_length

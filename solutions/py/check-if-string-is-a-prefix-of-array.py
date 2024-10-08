"""
Given a string s and an array of strings words, determine whether s is a prefix
string of words.
A string s is a prefix string of words if s can be made by concatenating the
first k strings in words for some positive k no larger than words.length.
Return true if s is a prefix string of words, or false otherwise.

Example 1:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters.
"""

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        j, n = 0, len(s)

        for word in words:
            if n - j < len(word):
                return False
            for letter in word:
                if letter != s[j]:
                    return False
                j += 1
            if j == n:
                return True

        return False


if __name__ == '__main__':
    sol = Solution()
    print(
        sol.isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"]))

"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character, but a character may map to
itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def counter(self, text):
        d = {}
        for i in text:
            d[i] = d.get(i, 0) + 1
        return d

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1:
            return True
        a = self.counter(s)
        b = self.counter(t)
        for i in range(1, len(s)):
            if (s[i - 1] == s[i]) != (t[i - 1] == t[i]) or a[s[i]] != b[t[i]]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.isIsomorphic(s="egg", t="add") is True
    assert sol.isIsomorphic(s="foo", t="bar") is False
    assert sol.isIsomorphic(s="paper", t="title") is True
    assert sol.isIsomorphic(s="bbbaaaba", t="aaabbbba") is False
    assert sol.isIsomorphic(s="badc", t="baba") is False

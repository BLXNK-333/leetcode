"""
Given a string s, return the maximum number of unique substrings that the given
string can be split into.
You can split string s into any list of non-empty substrings, where the
concatenation of the substrings forms the original string. However, you must
split the substrings such that all of them are unique.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc'].
Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and
'b' multiple times.

Example 2:
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

Constraints:
1 <= s.length <= 16
s contains only lower case English letters.
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        cnt = 0
        n = len(s)

        def bt(i=0, hs=None):
            nonlocal cnt
            if hs is None:
                hs = set()
            if i == n:
                if len(hs) > cnt:
                    cnt = len(hs)
                    return
            for j in range(i + 1, n + 1):
                part = s[i: j]
                if part not in hs:
                    bt(j, hs | {part})
        bt()
        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxUniqueSplit(s="ababccc"))
    print(sol.maxUniqueSplit(s="wwwzfvedwfvhsww"))

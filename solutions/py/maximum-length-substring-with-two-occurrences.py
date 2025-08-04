"""
Given a string s, return the maximum length of a substring such that it
contains at most two occurrences of each character.

Example 1:
Input: s = "bcbbbcba"
Output: 4
Explanation:
The following substring has a length of 4 and contains at most two occurrences
of each character: "bcbbbcba".

Example 2:
Input: s = "aaaa"
Output: 2
Explanation:
The following substring has a length of 2 and contains at most two occurrences
of each character: "aaaa".

Constraints:
2 <= s.length <= 100
s consists only of lowercase English letters.
"""

from collections import deque


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        dq = deque()
        hm = {}
        max_len = 0

        for a in s:
            hm[a] = hm.get(a, 0) + 1
            dq.append(a)

            if hm[a] == 3:
                while dq:
                    elem = dq[0]
                    hm[elem] = hm.get(elem) - 1
                    dq.popleft()
                    if elem == a and hm[elem] == 2:
                        break

            max_len = max(max_len, len(dq))

        return max_len


if __name__ == '__main__':
    sol = Solution()
    assert sol.maximumLengthSubstring(s="bcbbbcba") == 4
    assert sol.maximumLengthSubstring(s="aaaa") == 2
    assert sol.maximumLengthSubstring(s="eebadadbfa") == 9

    assert sol.maximumLengthSubstring(s="dcfdddccb") == 5

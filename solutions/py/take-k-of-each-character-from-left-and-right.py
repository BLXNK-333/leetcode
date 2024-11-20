"""
You are given a string s consisting of the characters 'a', 'b', and 'c' and a
non-negative integer k. Each minute, you may take either the leftmost character
of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each
character, or return -1 if it is not possible to take k of each character.

Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation:
Take three characters from the left of s. You now have two 'a' characters, and
one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two
'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

Constraints:
1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
"""


class Solution:
    def counter(self, seq):
        hm = {}
        for s in seq:
            hm[s] = hm.get(s, 0) + 1
        return hm

    def takeCharacters(self, s: str, k: int) -> int:
        if not k:
            return 0

        hm = self.counter(s)
        if k and len(hm) < 3 or any(map(lambda x: x < k, hm.values())):
            return -1

        n = min_del = len(s)
        i = j = 0

        while i <= j + 1 < n:
            while j < n:
                cur_j = s[j]
                nexxt = hm[cur_j] - 1
                if nexxt < k:
                    break
                j += 1
                hm[cur_j] = nexxt

            len_slide = n - j + i
            if len_slide < min_del:
                min_del = len_slide

            cur_i = s[i]
            hm[cur_i] = hm.get(cur_i, 0) + 1
            i += 1

        return min_del


if __name__ == '__main__':
    sol = Solution()

    assert sol.takeCharacters(s="aabaaaacaabc", k=2) == 8
    assert sol.takeCharacters(s="aabaaaacaabc", k=1) == 3
    assert sol.takeCharacters(s="aaaaaaaabcbc", k=2) == 6

    assert sol.takeCharacters(s="aabb", k=1) == -1
    assert sol.takeCharacters(s="abc", k=0) == 0

    assert sol.takeCharacters(s="aabbcc", k=2) == 6
    assert sol.takeCharacters(s="abc", k=1) == 3
    assert sol.takeCharacters(s="aabc", k=1) == 3

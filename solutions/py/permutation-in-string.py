"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or
false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def counter(self, s: str) -> dict:
        hm = {}
        for ltr in s:
            hm[ltr] = hm.get(ltr, 0) + 1
        return hm

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hmap = self.counter(s1)
        s1_len = len(s1)
        s2_len = len(s2)

        for i in range(s2_len - s1_len + 1):
            slide = self.counter(s2[i: i + s1_len])
            if s1_hmap == slide:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion(s1="ab", s2="eidbaooo"))
    print(sol.checkInclusion(s1="ab", s2="eidboaoo"))
    print(sol.checkInclusion(s1="adc", s2="dcda"))

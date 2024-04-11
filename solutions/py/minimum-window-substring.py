"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. If there
is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

from collections import deque


class Solution:
    def get_map(self, text: str) -> dict:
        hm = {}
        for letter in text:
            hm[letter] = hm.get(letter, 0) + 1
        return hm

    def comparator(self, unic: dict, target: dict) -> bool:
        for key in unic:
            if unic[key] > target.get(key, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        if len(t) == 1 and t in s:
            return t
        uniq_map = self.get_map(t)
        hash_map = {}
        queue = deque()
        min_length = float('inf')
        i = j = 0

        for index, value in enumerate(s):
            if value in uniq_map:
                queue.append((index, value))
                hash_map[value] = hash_map.get(value, 0) + 1
                while self.comparator(uniq_map, hash_map):
                    pop_i, pop_v = queue.popleft()
                    candidate = queue[-1][0] - pop_i + 1
                    if candidate < min_length:
                        min_length = candidate
                        i, j = pop_i, queue[-1][0]
                    hash_map[pop_v] -= 1

        return '' if min_length == float('inf') else s[i: j + 1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert sol.minWindow(s="a", t="a") == "a"
    assert sol.minWindow(s="a", t="aa") == ""
    assert sol.minWindow(s="aa", t="aa") == "aa"

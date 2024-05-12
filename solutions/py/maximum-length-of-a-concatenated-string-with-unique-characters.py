"""
You are given an array of strings arr. A string s is formed by the
concatenation of a subsequence of arr that has unique characters.
Return the maximum possible length of s.
A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers")
and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""

from typing import List


class Solution:
    def removeDuplicate(self, arr: List[str]) -> List[str]:
        new_arr = []
        for seq in arr:
            if len(seq) == len(set(seq)):
                new_arr.append(seq)
        return new_arr

    def set_bit(self, mask: int, n: int):
        return mask | (1 << n)

    def get_bit(self, mask: int, n: int):
        return (mask >> n) & 1

    def is_valid_tail(self, mask: int, tail: str):
        for letter in tail:
            cur_bit = ord(letter) - 97
            if self.get_bit(mask, cur_bit):
                return False
        return True

    def attach_the_tail(self, mask: int, tail: str):
        for letter in tail:
            cur_bit = ord(letter) - 97
            mask = self.set_bit(mask, cur_bit)
        return mask

    def maxLength(self, arr: List[str]) -> int:
        clean_arr = self.removeDuplicate(arr)
        n = len(clean_arr)
        max_bit_len = 0

        def backtracking(mask: int = 0, cur_cnt: int = 0, index: int = 0):
            nonlocal max_bit_len

            if index > n:
                return
            if cur_cnt > max_bit_len:
                max_bit_len = cur_cnt
            for i in range(index, n):
                tail = clean_arr[i]
                if self.is_valid_tail(mask, tail):
                    new_mask = self.attach_the_tail(mask, tail)
                    backtracking(new_mask, cur_cnt + len(tail), i + 1)

        backtracking()
        return max_bit_len


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxLength(arr=["un", "iq", "ue"]) == 4
    assert sol.maxLength(arr=["cha", "r", "act", "ers"]) == 6
    assert sol.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]) == 26

    assert sol.maxLength(arr=["aa", "bb"]) == 0

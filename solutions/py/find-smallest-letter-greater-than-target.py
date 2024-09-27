"""
You are given an array of characters letters that is sorted in non-decreasing
order, and a character target. There are at least two different characters in
letters.
Return the smallest character in letters that is lexicographically greater than
target. If such a character does not exist, return the first character in
letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a'
in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c'
in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically
greater than 'z' so we return letters[0].

Constraints:
2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        L, R = -1, len(letters)
        target_num = ord(target)

        while L + 1 < R:
            M = (L + R) // 2
            if ord(letters[M]) > target_num:
                R = M
            else:
                L = M
        if R == len(letters):
            return letters[0]
        return letters[R]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
    print(sol.nextGreatestLetter(letters=["c", "f", "j"], target="c"))
    print(sol.nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))

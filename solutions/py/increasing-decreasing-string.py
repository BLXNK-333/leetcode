"""
You are given a string s. Reorder the string using the following algorithm:
Remove the smallest character from s and append it to the result.
Remove the smallest character from s that is greater than the last appended
character, and append it to the result.
Repeat step 2 until no more characters can be removed.
Remove the largest character from s and append it to the result.
Remove the largest character from s that is smaller than the last appended
character, and append it to the result.
Repeat step 5 until no more characters can be removed.
Repeat steps 1 through 6 until all characters from s have been removed.
If the smallest or largest character appears more than once, you may choose any
occurrence to append to the result.
Return the resulting string after reordering s using this algorithm.

Example 1:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the
mentioned algorithm.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.
"""


class Solution:
    def __init__(self):
        self._array = [0] * 26
        self._result = []

    def sortString(self, s: str) -> str:
        self._count_letters(s)

        while len(self._result) < len(s):
            self._remove_the_smallest()
            self._remove_the_largest()

        return "".join(self._result)

    def _count_letters(self, s: str):
        for let in s:
            self._array[ord(let) - 97] += 1

    def _remove_the_smallest(self):
        for i in range(26):
            amt = self._array[i]
            if amt > 0:
                val = chr(97 + i)
                self._result.append(val)
                self._array[i] -= 1

    def _remove_the_largest(self):
        for i in range(25, -1, -1):
            amt = self._array[i]
            if amt > 0:
                val = chr(97 + i)
                self._result.append(val)
                self._array[i] -= 1


if __name__ == '__main__':
    sol = Solution()
    assert sol.sortString(s = "aaaabbbbcccc") == "abccbaabccba"

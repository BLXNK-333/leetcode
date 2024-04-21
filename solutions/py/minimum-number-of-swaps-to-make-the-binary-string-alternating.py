"""
Given a binary string s, return the minimum number of character swaps to make it alternating, or
-1 if it is impossible.
The string is called alternating if no two adjacent characters are equal. For example, the
strings "010" and "1010" are alternating, while the string "0100" is not.
Any two characters may be swapped, even if they are not adjacent.

Example 1:
Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.

Example 2:
Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.

Example 3:
Input: s = "1110"
Output: -1

Constraints:
1 <= s.length <= 1000
s[i] is either '0' or '1'.
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        if len(s) == 1:
            return 0
        null = s.count("0")
        ones = s.count("1")
        if abs(null - ones) > 1:
            return -1

        if null > ones:
            return self.counter("0", s)
        elif null < ones:
            return self.counter("1", s)
        else:
            return min(self.counter("0", s), self.counter("1", s))

    @staticmethod
    def counter(start: str, s: str):
        cnt = 0
        for i in range(len(s)):
            if s[i] != start:
                cnt += 1
            start = "0" if start == "1" else "1"
        return cnt // 2


if __name__ == '__main__':
    sol = Solution()
    bad = ("11100000001000010101001010100001010101010010000011101010000101111011"
           "00000111110001000111010111101100001100001001100101011110100011111100"
           "00000010001111101111011111101111011101010011110101111111110110110010"
           "1010110000011110110100101111000100000001100000")
    assert sol.minSwaps(bad) == 60

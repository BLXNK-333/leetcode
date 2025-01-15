"""
Given two positive integers num1 and num2, find the positive integer x such
that:
x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.
Return the integer x. The test cases are generated such that x is uniquely
determined.
The number of set bits of an integer is the number of 1's in its binary
representation.

Example 1:
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 =
0 is minimal.

Example 2:
Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 =
2 is minimal.

Constraints:
1 <= num1, num2 <= 109
"""


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1_len, n2_len = num1.bit_count(), num2.bit_count()
        diff = n1_len - n2_len
        i = 0

        while diff > 0:
            if num1 & (1 << i):
                num1 ^= (1 << i)
                diff -= 1
            i += 1

        while diff < 0:
            if not (num1 & (1 << i)):
                num1 ^= (1 << i)
                diff += 1
            i += 1

        return num1


if __name__ == '__main__':
    sol = Solution()
    assert sol.minimizeXor(num1=3, num2=5) == 3
    assert sol.minimizeXor(num1=1, num2=12) == 3
    assert sol.minimizeXor(num1=25, num2=72) == 24

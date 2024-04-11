"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you
can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the
string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".

Constraints:
1 <= s.length <= 104
s[i] is either '0' or '1'.
"""

class Solution:
    def counter(self, pattern, S):
        a, b = pattern
        count = 0
        for i in range(len(S)):
            if i & 1:
                if S[i] != b:
                    count += 1
            elif S[i] != a:
                count += 1
        return count

    def minOperations(self, s: str) -> int:
        return min(self.counter(['0', '1'], s), self.counter(['1', '0'], s))


if __name__ == '__main__':
    sol = Solution()
    assert sol.minOperations("0100") == 1
    assert sol.minOperations("10") == 0
    assert sol.minOperations("1111") == 2
    assert sol.minOperations("01001") == 2
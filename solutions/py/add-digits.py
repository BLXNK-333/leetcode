"""
Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 231 - 1
Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str(sum(map(int, str_num)))

        return int(str_num)


if __name__ == '__main__':
    sol = Solution()

    for i in range(100):
        print(f"{i}. ", end="")
        print(sol.addDigits(i))
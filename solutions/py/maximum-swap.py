"""
You are given an integer num. You can swap two digits at most once to get the
maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
0 <= num <= 108
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        result = num
        str_num = str(num)
        n = len(str_num)

        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = list(str_num)
                temp[i], temp[j] = temp[j], temp[i]
                x = int("".join(temp))
                if x > result:
                    result = x
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSwap(2736))
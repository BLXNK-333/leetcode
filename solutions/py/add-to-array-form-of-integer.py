"""
The array-form of an integer num is an array representing its digits in left to
right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-
form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Constraints:
1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104
"""

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k_arr = []
        while k != 0:
            k, y = divmod(k, 10)
            k_arr.append(y)
        k_arr = k_arr[::-1]

        n, m = len(num), len(k_arr)
        max_len = max(n, m)

        if n != max_len:
            num = [0] * (max_len - n) + num
        if m != max_len:
            k_arr = [0] * (max_len - m) + k_arr

        res, rem = [], 0

        for i in range(max_len - 1, -1, -1):
            x = num[i] + k_arr[i] + rem
            rem, x = divmod(x, 10)
            res.append(x)

        if rem:
            res.append(rem)

        return res[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.addToArrayForm(num=[1, 2, 0, 0], k=34))
    print(sol.addToArrayForm(num=[2, 7, 4], k=181))
    print(sol.addToArrayForm(num=[2, 1, 5], k=806))

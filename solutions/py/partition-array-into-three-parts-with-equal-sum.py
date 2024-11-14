"""
Given an array of integers arr, return true if we can partition the array into
three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with
(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1]
== arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Constraints:
3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104
"""

from typing import List


class Solution:
    def find_part_sum(self, start_index: int, part_sum: int, array: List[int]):
        s = 0
        for i in range(start_index, len(array)):
            s += array[i]
            if s == part_sum:
                return i + 1
        return -1

    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        S = sum(arr)
        if S % 3:
            return False
        part = S // 3

        a = self.find_part_sum(0, part, arr)
        if a < 0:
            return False

        b = self.find_part_sum(a, part, arr)
        if b < 0:
            return False

        c = self.find_part_sum(b, part, arr)
        if c < 0:
            return False

        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.canThreePartsEqualSum(
        [29, 31, 27, -10, -67, 22, 15, -1, -16, -29, 59, -18, 48]) == True
    assert sol.canThreePartsEqualSum([0, 0, 0, 0]) == True

    assert sol.canThreePartsEqualSum([1, -1, 1, -1]) == False

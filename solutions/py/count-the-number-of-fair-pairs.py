"""
Given a 0-indexed integer array nums of size n and two integers lower and
upper, return the number of fair pairs.
A pair (i, j) is fair if:
0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and
(1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

Constraints:
1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
"""

from typing import List


class Solution:
    def _left_binary_search(self, i: int, lower: int, nums: List[int]) -> int:
        L, R = i, len(nums)
        while L + 1 < R:
            M = (L + R) // 2
            S = nums[i] + nums[M]
            if S >= lower:
                R = M
            else:
                L = M
        return R

    def _right_binary_search(self, i: int, upper: int, nums: List[int]) -> int:
        L, R = i, len(nums)
        while L + 1 < R:
            M = (L + R) // 2
            S = nums[i] + nums[M]
            if S <= upper:
                L = M
            else:
                R = M
        return L

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        cnt = 0
        nums.sort()

        for i in range(len(nums)):
            L = self._left_binary_search(i, lower, nums)
            R = self._right_binary_search(i, upper, nums)
            diff = R - L + 1
            if diff < 0:
                break
            cnt += diff

        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.countFairPairs([0, 1, 4, 4, 5, 7], 3, 6))
    print(sol.countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11))

"""
Given an integer array nums, return the largest perimeter of a triangle with a
non-zero area, formed from three of these lengths. If it is impossible to form
any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:
Input: nums = [1,2,1,10]
Output: 0
Explanation:
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we
return 0.

Constraints:
3 <= nums.length <= 104
1 <= nums[i] <= 106
"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)

        i, j, h = 0, 1, 2

        while h < n:
            a_plus_b = nums[j] + nums[h]
            if a_plus_b > nums[i]:
                return a_plus_b + nums[i]

            i, j, h = j, h, h + 1

        return 0

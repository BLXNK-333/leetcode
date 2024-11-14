"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
Follow up: Could you minimize the total number of operations done?
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        new_nums = [n for n in nums if n]
        new_nums.extend([0] * (length - len(new_nums)))
        nums.clear()
        nums.extend(new_nums)


if __name__ == '__main__':
    array = [0, 1, 0, 3, 12]
    sol = Solution()
    sol.moveZeroes(array)

    print(array)
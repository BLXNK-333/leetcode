"""
There is an integer array nums sorted in ascending order (with distinct
values).
Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
[4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return
the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

from typing import List


class Solution:
    def get_lowest_item_idx(self, nums):
        L, R, target = -1, len(nums), nums[-1]
        while L + 1 < R:
            M = (L + R) // 2
            if nums[M] == target:
                return M
            if nums[M] > target:
                L = M
            else:
                R = M
        return R

    def bs(self, L, R, nums, target):
        while L + 1 < R:
            M = (L + R) // 2
            if nums[M] == target:
                return M
            if nums[M] > target:
                R = M
            else:
                L = M
        return -1

    def search(self, nums: List[int], target: int) -> int:
        low_idx = self.get_lowest_item_idx(nums)
        if low_idx:
            left_part = self.bs(-1, low_idx + 1, nums, target)
            if left_part != -1:
                return left_part
            return self.bs(low_idx - 1, len(nums), nums, target)
        else:
            return self.bs(-1, len(nums), nums, target)


if __name__ == '__main__':
    sol = Solution()
    assert sol.search(nums = [4,5,6,7,0,1,2], target = 0) == 4
    assert sol.search(nums = [4,5,6,7,0,1,2], target = 3) == -1
    assert sol.search(nums = [1], target = 0) == -1
    assert sol.search(nums = [1, 3], target = 3) == 1

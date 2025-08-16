"""
We define a harmonious array as an array where the difference between its
maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious
subsequence among all its possible subsequences.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which
have a length of 2.

Example 3:
Input: nums = [1,1,1,1]
Output: 0
Explanation:
No harmonic subsequence exists.

Constraints:
1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
"""

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        min_idx = 0

        for i in range(1, len(nums)):
            if nums[min_idx] == nums[i]:
                continue
            while nums[i] - nums[min_idx] > 1:
                min_idx += 1
            diff = i - min_idx + 1
            if diff > longest:
                longest = diff

        return longest if longest > 1 else 0


if __name__ == '__main__':
    sol = Solution()
    assert sol.findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 7]) == 5
    assert sol.findLHS(nums=[1, 2, 3, 4]) == 2
    assert sol.findLHS(nums=[1, 1, 1, 1]) == 0

    assert sol.findLHS([1, 3, 5, 7, 9, 11, 13, 15, 17]) == 0

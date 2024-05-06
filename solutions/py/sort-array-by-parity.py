"""
Given an integer array nums, move all the even integers at the beginning of the array followed
by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        while True:
            while i <= j and not nums[i] % 2:
                i += 1
            while j >= i and nums[j] % 2:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArrayByParity([3, 1, 2, 4]))
    print(sol.sortArrayByParity([0, 2]))
    print(sol.sortArrayByParity([0]))
    print(sol.sortArrayByParity([1, 2, 3, 4, 5, 6, 7, 8]))

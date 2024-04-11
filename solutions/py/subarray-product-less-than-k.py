"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays
where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums.append(1)
        j = -1
        current = 1
        counter = 0
        for i in range(len(nums) - 1):
            current *= nums[i]
            while j < i and (x := current // nums[j]) >= k:
                current = x
                j += 1
            counter += (i - j)
        return counter


if __name__ == '__main__':
    sol = Solution()
    assert sol.numSubarrayProductLessThanK([10, 5, 2, 6], k=100) == 8
    assert sol.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0) == 0
    assert sol.numSubarrayProductLessThanK(nums=[10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], k=19) == 18

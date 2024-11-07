"""
Given an array nums, return true if the array was originally sorted in non-
decreasing order, then rotated some number of positions (including zero).
Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same
length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of
value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def _find_min_index(self, array: List[int]):
        j = 0
        for i in range(len(array)):
            if array[i] < array[j]:
                j = i
        return j

    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        j = self._find_min_index(nums)

        i = 1
        while True:
            prev_j = (j - 1) % n
            if nums[j] == nums[prev_j]:
                j = prev_j
                i += 1
                if i == n:
                    return True
            else:
                break

        i = 1
        while i < n:
            next_j = (j + 1) % n
            if nums[j] <= nums[next_j]:
                j = next_j
                i += 1
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.check(nums=[3, 4, 5, 1, 2]) == True
    assert sol.check(nums=[2, 1, 3, 4]) == False
    assert sol.check(nums=[6, 10, 6]) == True
    assert sol.check(nums=[6, 6, 6]) == True
    assert sol.check(nums=[6]) == True

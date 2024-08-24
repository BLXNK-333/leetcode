"""
You are given an array of integers nums. Return the length of the longest
subarray of nums which is either strictly increasing or strictly decreasing.

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and
[1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2],
and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and
[3,2,1].
Hence, we return 3.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50
"""

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_cnt = cur_cnt = 1
        array = nums + nums[::-1] + [51]

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                cur_cnt += 1
            else:
                if cur_cnt > max_cnt:
                    max_cnt = cur_cnt
                cur_cnt = 1

        return max_cnt


if __name__ == '__main__':
    sol = Solution()

    assert sol.longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2
    assert sol.longestMonotonicSubarray([3, 3, 3, 3]) == 1
    assert sol.longestMonotonicSubarray([3, 2, 1]) == 3

    assert sol.longestMonotonicSubarray([1, 2]) == 2

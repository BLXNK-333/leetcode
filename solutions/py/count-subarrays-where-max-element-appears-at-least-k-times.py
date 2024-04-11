"""
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in
that subarray.
A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3],
[1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        A = [j for j in range(n) if nums[j] == mx]
        total = i = j = 0
        while (x := j + k) <= len(A):
            total += (n - A[x - 1])
            if i == A[j]:
                j += 1
            i += 1
        return total


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubarrays([1, 3, 2, 3, 3], k=2))
    print(sol.countSubarrays([1, 4, 2, 1], k=3))
    print(sol.countSubarrays([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], k=2))

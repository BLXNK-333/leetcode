"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3],
[1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:
1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""

from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = j = 0
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
            while len(hash_map) > k:
                hash_map[nums[j]] -= 1
                if not hash_map[nums[j]]:
                    del hash_map[nums[j]]
                j += 1
            if len(hash_map) == k:
                hash_map_2 = hash_map.copy()
                x = j
                while len(hash_map_2) == k:
                    counter += 1
                    hash_map_2[nums[x]] -= 1
                    if not hash_map_2[nums[x]]:
                        del hash_map_2[nums[x]]
                    x += 1

        return counter


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
    print(sol.subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
    print(sol.subarraysWithKDistinct(nums=[2, 1, 1, 1, 2], k=1))

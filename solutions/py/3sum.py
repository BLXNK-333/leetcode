"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i !=
j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List


class Solution:
    def counter(self, arr):
        d = {}
        for i, val in enumerate(arr):
            d[val] = i
        return d

    def cheat(self, arr):
        if arr[0] == 0:
            return [[0, 0, 0]]
        else:
            return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hmap = self.counter(nums)
        if len(hmap) == 1:
            return self.cheat(nums)

        n = len(nums)
        result = set()

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                x = 0 - (nums[i] + nums[j])
                if x in hmap and hmap[x] > j:
                    new_three = tuple(sorted([nums[i], nums[j], x]))
                    if new_three not in result:
                        result.add(new_three)
        return [list(three) for three in result]


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))

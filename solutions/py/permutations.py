"""
Given an array nums of distinct integers, return all the possible permutations. You can return
the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        array = []

        def rec(box: list, perm: list = None):
            if not perm:
                perm = []
            if not box:
                array.append(perm)
            else:
                for i in range(len(box)):
                    rec(box[:i] + box[i + 1:], perm + [box[i]])

        rec(nums)
        return array


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))

"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique
permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        array = []

        def rec(box: list, perm: list = None):
            if not perm:
                perm = []
            if not box:
                array.append(perm)
            else:
                uniq = set()
                for i in range(len(box)):
                    if box[i] not in uniq:
                        uniq.add(box[i])
                        rec(box[:i] + box[i + 1:], perm + [box[i]])
        rec(nums)
        return array


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([3,3,0,3]))
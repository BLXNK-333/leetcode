"""
Given a set of distinct positive integers nums, return the largest subset answer such that every
pair (answer[i], answer[j]) of elements in this subset satisfies:
answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        hash_map = {0: [nums[0]]}

        for i in range(1, len(nums)):
            j = i - 1
            prev = []
            while j > -1:
                if not nums[i] % nums[j] and len(hash_map.get(j)) > len(prev):
                    prev = hash_map.get(j)
                j -= 1
            hash_map[i] = prev + [nums[i]]
        return max(hash_map.values(), key=len)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestDivisibleSubset([4, 8, 10, 240]))

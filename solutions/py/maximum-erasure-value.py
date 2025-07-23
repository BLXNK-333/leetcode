"""
You are given an array of positive integers nums and want to erase a subarray
containing unique elements. The score you get by erasing the subarray is equal
to the sum of its elements.
Return the maximum score you can get by erasing exactly one subarray.
An array b is called to be a subarray of a if it forms a contiguous subsequence
of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

from typing import List
from collections import deque


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hset = set()
        dq = deque([])
        cur_sum = max_sum = 0

        for d in nums:
            if d in hset:
                if cur_sum > max_sum:
                    max_sum = cur_sum
                while dq:
                    cur = dq.popleft()
                    cur_sum -= cur
                    hset.discard(cur)
                    if cur == d:
                        break

            cur_sum += d
            hset.add(d)
            dq.append(d)

        return max(cur_sum, max_sum)


if __name__ == '__main__':
    sol = Solution()
    assert sol.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]) == 17
    assert sol.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
    assert sol.maximumUniqueSubarray(
        nums=[187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411,
              459, 490, 266, 987, 965, 429, 166, 809, 340, 467, 318, 125, 165, 809, 610,
              31, 585, 970, 306, 42, 189, 169, 743, 78, 810, 70, 382, 367, 490, 787, 670,
              476, 278, 775, 673, 299, 19, 893, 817, 971, 458, 409, 886, 434]
    ) == 16911

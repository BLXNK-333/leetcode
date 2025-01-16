"""
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative
integers. There exists another array, nums3, which contains the bitwise XOR of
all pairings of integers between nums1 and nums2 (every integer in nums1 is
paired with every integer in nums2 exactly once).
Return the bitwise XOR of all integers in nums3.

Example 1:
Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^
nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.

Constraints:
1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[j] <= 109
"""

from typing import List
from functools import reduce


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1) & 1, len(nums2) & 1

        if not n and not m:
            return 0

        n2_xor = reduce(lambda x, y: x ^ y, nums2)
        if n and not m:
            return n2_xor

        n1_xor = reduce(lambda x, y: x ^ y, nums1)
        if not n and m:
            return n1_xor

        return n1_xor ^ n2_xor


if __name__ == '__main__':
    sol = Solution()
    assert sol.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]) == 13
    assert sol.xorAllNums(nums1=[1, 2], nums2=[3, 4]) == 0
    assert sol.xorAllNums(nums1=[1, 2, 3], nums2=[5, 4]) == 1
    assert sol.xorAllNums(nums1=[2, 1, 3, 4, 5, 78, 100], nums2=[10, 2, 5, 0, 3]) == 37

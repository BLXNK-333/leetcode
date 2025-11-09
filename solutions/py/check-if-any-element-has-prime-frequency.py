"""
You are given an integer array nums.
Return true if the frequency of any element of the array is prime, otherwise,
return false.
The frequency of an element x is the number of times it occurs in the array.
A prime number is a natural number greater than 1 with only two factors, 1 and
itself.

Example 1:
Input: nums = [1,2,3,4,5,4]
Output: true
Explanation:
4 has a frequency of two, which is a prime number.

Example 2:
Input: nums = [1,2,3,4,5]
Output: false
Explanation:
All elements have a frequency of one.

Example 3:
Input: nums = [2,2,2,4,4]
Output: true
Explanation:
Both 2 and 4 have a prime frequency.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def _is_prime(self, num: int) -> bool:
        if num <= 1:
            return False

        d = 2
        while d * d <= num:
            if not num % d:
                return False
            d += 1
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        hm = {}
        for d in nums:
            hm[d] = hm.get(d, 0) + 1

        for v in set(hm.values()):
            if self._is_prime(v):
                return True

        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.checkPrimeFrequency(nums=[1, 2, 3, 4, 5, 4]) == True
    assert sol.checkPrimeFrequency(nums=[1, 2, 3, 4, 5]) == False
    assert sol.checkPrimeFrequency(nums=[2, 2, 2, 4, 4]) == True
    assert sol.checkPrimeFrequency(nums=[3, 0, 3, 6, 3, 3]) == False

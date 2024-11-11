"""
You are given a 0-indexed integer array nums of length n.
You can perform the following operation as many times as you want:
Pick an index i that you haven’t picked before, and pick a prime p strictly
less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above
operation and false otherwise.
A strictly increasing array is an array whose each element is strictly greater
than its preceding element.

Example 1:
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3
from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes
equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the
answer is true.

Example 2:
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't
need to make any operations.

Example 3:
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to
make nums sorted in strictly increasing order, so the answer is false.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
"""

from typing import List


class Solution:
    def get_primes(self, n=1000):
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False

        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False

        primes = [p for p in range(n + 1) if is_prime[p]]
        return primes

    def binary_search(self, number: int, nexxt: int, array: List[int]) -> int:
        L, R = -1, len(array)
        while L + 1 < R:
            M = (L + R) // 2
            if number - array[M] < nexxt:
                R = M
            else:
                L = M
        if R == len(array):
            return number
        result = number - array[R]
        if result < 1:
            return number
        return result

    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True

        primes = self.get_primes()
        i = n - 2
        nexxt = nums[n - 1]

        while i > -1:
            if nums[i] >= nexxt:
                new_num = self.binary_search(nums[i], nexxt, primes)
                if new_num >= nexxt:
                    return False
                nums[i] = new_num

            nexxt = nums[i]
            i -= 1

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.primeSubOperation(nums=[6, 8, 11, 12]))

"""
You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return true if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers rule and
false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, length = 0, len(flowerbed)
        m_len = length - 1

        while n and i < length:
            if flowerbed[i]:
                i += 2
                continue

            if flowerbed[min(i + 1, m_len)]:
                i += 3
                continue

            if flowerbed[max(0, i - 1)]:
                i += 1
                continue

            n -= 1
            i += 2

        return not n


if __name__ == '__main__':
    sol = Solution()
    assert sol.canPlaceFlowers(flowerbed=[1, 0, 1, 0, 1, 0, 1], n=1) == 0
    assert sol.canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1) == 1
    assert sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1, 0, 0], n=2) == 1
    assert sol.canPlaceFlowers(flowerbed=[0, 1, 0, 1, 0, 1, 0, 0], n=1) == 1
    assert sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2) == 0

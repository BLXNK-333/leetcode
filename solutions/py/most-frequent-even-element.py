"""
Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return
-1.

Example 1:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

Example 2:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.

Example 3:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

Constraints:
1 <= nums.length <= 2000
0 <= nums[i] <= 105
"""

from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if not num % 2:
                hm[num] = hm.get(num, 0) + 1

        if not len(hm):
            return -1

        max_freq = max(hm.values())
        return min(t[0] for t in hm.items() if t[1] == max_freq)


if __name__ == '__main__':
    sol = Solution()
    print(sol.mostFrequentEven(
        [8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]))

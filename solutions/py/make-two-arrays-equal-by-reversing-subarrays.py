"""
You are given two integer arrays of equal length target and arr. In one step,
you can select any non-empty subarray of arr and reverse it. You are allowed to
make any number of steps.
Return true if you can make arr equal to target or false otherwise.

Example 1:
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to
do so.

Example 2:
Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.

Example 3:
Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.

Constraints:
target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
"""

from typing import List, Dict


class Solution:
    def counter(self, array: List[int]) -> Dict[int, int]:
        hm = {}
        for n in array:
            hm[n] = hm.get(n, 0) + 1
        return hm

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hm1 = self.counter(target)
        hm2 = self.counter(arr)

        if len(hm1) != len(hm2):
            return False

        for k, v in hm1.items():
            if k not in hm2 or hm2[k] != v:
                return False
        return True
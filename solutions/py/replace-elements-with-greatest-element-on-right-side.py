"""
Given an array arr, replace every element in that array with the greatest
element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.

Constraints:
1 <= arr.length <= 104
1 <= arr[i] <= 105
"""

from typing import List, Tuple


class Solution:
    def _find_max_val(self, arr: List[int], start_idx: int) -> Tuple[int, int]:
        max_idx = max_val = 0
        n = len(arr)

        for i in range(start_idx, n):
            if arr[i] >= max_val:
                max_idx, max_val = i, arr[i]

        return max_idx, max_val

    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        max_idx = max_val = 0

        for i in range(n - 1):
            if max_idx <= i:
                max_idx, max_val = self._find_max_val(arr, i + 1)
            result.append(max_val)
        result.append(-1)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceElements(arr=[17, 18, 5, 4, 6, 1]))

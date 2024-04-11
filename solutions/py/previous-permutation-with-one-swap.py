"""
Given an array of positive integers arr (not necessarily distinct), return the lexicographically
largest permutation that is smaller than arr, that can be made with exactly one swap. If it
cannot be done, then return the same array.
Note that a swap exchanges the positions of two numbers arr[i] and arr[j]

Example 1:
Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.

Example 2:
Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.

Example 3:
Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.

Constraints:
1 <= arr.length <= 104
1 <= arr[i] <= 104
"""

from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            return arr

        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        if i == -1:
            return arr

        j = n - 1
        while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]
        return arr


if __name__ == '__main__':
    sol = Solution()
    # assert sol.prevPermOpt1([3, 2, 1]) == [3, 1, 2]
    # assert sol.prevPermOpt1([1, 1, 5]) == [1, 1, 5]
    # assert sol.prevPermOpt1([1, 9, 4, 6, 7]) == [1, 7, 4, 6, 9]
    assert sol.prevPermOpt1([3, 1, 1, 3]) == [1, 3, 1, 3]

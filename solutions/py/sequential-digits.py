"""
An integer has sequential digits if and only if each digit in the number is one more than the
previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential
digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:
10 <= low <= high <= 10^9
"""

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        numbers = list(range(1, 10))

        def rec(st: int = 0, en: int = 8, comb: int = 0):
            if low <= comb <= high:
                result.append(comb)
            for i in range(st, en):
                new_comb = comb * 10 + numbers[i]
                if new_comb > high:
                    break
                rec(i + 1, min(i + 2, 9), new_comb)

        rec()
        return sorted(result)


if __name__ == '__main__':
    sol = Solution()
    assert sol.sequentialDigits(low=1000, high=13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    assert sol.sequentialDigits(low=100, high=300) == [123, 234]

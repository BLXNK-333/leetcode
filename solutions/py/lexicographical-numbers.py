"""
Given an integer n, return all the numbers in the range [1, n] sorted in
lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]

Constraints:
1 <= n <= 5 * 104
"""

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def rec(cur: int = 1):
            for i in range(cur, cur + 10 - (1 if cur == 1 else 0)):
                if i > n:
                    break
                result.append(i)
                rec(i * 10)

        rec()
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.lexicalOrder(34))

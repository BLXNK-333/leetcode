"""
An integer x is numerically balanced if for every digit d in the number x, there are exactly d
occurrences of that digit in x.
Given an integer n, return the smallest numerically balanced number strictly greater than n.

Example 1:
Input: n = 1
Output: 22
Explanation:
22 is numerically balanced since:
- The digit 2 occurs 2 times.
It is also the smallest numerically balanced number strictly greater than 1.

Example 2:
Input: n = 1000
Output: 1333
Explanation:
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.

Example 3:
Input: n = 3000
Output: 3133
Explanation:
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.

Constraints:
0 <= n <= 106
"""

class Solution:
    def is_balanced(self, comb: dict):
        for number in range(1, 7):
            if comb[number] and comb[number] != number:
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        if not n:
            return 1

        nearest = 1224444
        max_num = min(n * 100, nearest)
        stack = [[0] * 7]

        while stack:
            comb = stack.pop()
            current_num = comb[0]

            if current_num > max_num or current_num > nearest:
                continue

            if n < current_num < nearest and self.is_balanced(comb):
                nearest = current_num
                continue

            for i in range(1, 7):
                if comb[i] + 1 <= i:
                    next_comb = comb.copy()
                    next_comb[i] += 1
                    next_comb[0] = current_num * 10 + i
                    stack.append(next_comb)

        return nearest


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextBeautifulNumber(10461))
    print(sol.nextBeautifulNumber(3000))
    print(sol.nextBeautifulNumber(3314))
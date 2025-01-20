"""
There is a bookstore owner that has a store open for n minutes. You are given
an integer array customers of length n where customers[i] is the number of the
customers that enter the store at the start of the ith minute and all those
customers leave after the end of that minute.
During certain minutes, the bookstore owner is grumpy. You are given a binary
array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the
ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers entering during that minute
are not satisfied. Otherwise, they are satisfied.
The bookstore owner knows a secret technique to remain not grumpy for minutes
consecutive minutes, but this technique can only be used once.
Return the maximum number of customers that can be satisfied throughout the
day.

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation:
The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 =
16.

Example 2:
Input: customers = [1], grumpy = [0], minutes = 1
Output: 1

Constraints:
n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
"""

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        customers = [1,0,1,2,1,1,7,5],
        grumpy = [0,1,0,1,0,1,0,1],
        minutes = 3
        """
        n = len(customers)
        i = j = max_remain = cur_remain = mi = mj = 0

        while j < n:
            if minutes:
                if grumpy[j]:
                    max_remain += customers[j]
                cur_remain = max_remain
                j += 1
                mj = j
                minutes -= 1
            else:
                if grumpy[i]:
                    cur_remain -= customers[i]
                if grumpy[j]:
                    cur_remain += customers[j]
                i += 1
                j += 1

                if cur_remain > max_remain:
                    max_remain = cur_remain
                    mi, mj = i, j

        result = 0

        for i in range(n):
            if i < mi or i >= mj:
                if not grumpy[i]:
                    result += customers[i]
            else:
                result += customers[i]

        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5],
                           grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3) == 16
    assert sol.maxSatisfied(customers=[1], grumpy=[0], minutes=1) == 1
    assert sol.maxSatisfied(customers=[4, 10, 10], grumpy=[1, 1, 0], minutes=2) == 24
    assert sol.maxSatisfied(customers=[7, 8, 8, 6], grumpy=[0, 1, 0, 1], minutes=3) == 29

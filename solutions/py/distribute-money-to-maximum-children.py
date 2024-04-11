"""
You are given an integer money denoting the amount of money (in dollars) that you have and
another integer children denoting the number of children that you must distribute the money to.
You have to distribute the money according to the following rules:
All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the
money according to the aforementioned rules. If there is no way to distribute the money, return
-1.

Example 1:
Input: money = 20, children = 3
Output: 1
Explanation:
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money
is:
- 8 dollars to the first child.
- 9 dollars to the second child.
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is
greater than 1.

Example 2:
Input: money = 16, children = 2
Output: 2
Explanation: Each child can be given 8 dollars.

Constraints:
1 <= money <= 200
2 <= children <= 30
"""

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money < 8:
            return 0

        eight = 0
        while children:
            x = money - 8
            if x < children - 1:
                break
            money = x
            children -= 1
            eight += 1
        if money == 4 and children == 1 or children == 0 and money > 0:
            return eight - 1
        return eight


if __name__ == '__main__':
    sol = Solution()
    assert sol.distMoney(2, 2) == 0
    assert sol.distMoney(20, 3) == 1
    assert sol.distMoney(16, 2) == 2

    assert sol.distMoney(4, 2) == 0
    assert sol.distMoney(8, 1) == 1
    assert sol.distMoney(7, 8) == -1

    assert sol.distMoney(9, 8) == 0
    assert sol.distMoney(12, 3) == 1
    assert sol.distMoney(17, 2) == 1
    assert sol.distMoney(23, 2) == 1
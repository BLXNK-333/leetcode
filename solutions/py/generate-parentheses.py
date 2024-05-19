"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(lb=0, rb=0, comb=""):
            if lb == n and rb == n:
                result.append(comb)
            else:
                if lb > rb:
                    dfs(lb, rb + 1, comb + ")")
                if lb < n:
                    dfs(lb + 1, rb, comb + "(")

        dfs()
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))

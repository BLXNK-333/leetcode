"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hm = {"]": "[", "}": "{", ")": "("}

        for br in s:
            if not stk:
                stk.append(br)
            elif br in hm:
                if stk[-1] != hm[br]:
                    return False
                stk.pop()
            else:
                stk.append(br)
        return not stk


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))

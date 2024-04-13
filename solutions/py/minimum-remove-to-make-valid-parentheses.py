"""
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so
that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        lb = rb = 0
        for i in range(len(s)):
            if s[i] == "(":
                lb += 1
            elif s[i] == ")":
                new_rb = rb + 1
                if new_rb > lb:
                    continue
                rb = new_rb
            stack.append(s[i])

        lb = rb = 0
        rev_stack = []
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == ")":
                rb += 1
            elif stack[i] == "(":
                new_lb = lb + 1
                if new_lb > rb:
                    continue
                lb = new_lb
            rev_stack.append(stack[i])
        return "".join(rev_stack[::-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee))))((((((t(c)o)de)"))
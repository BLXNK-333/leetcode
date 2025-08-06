"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A
and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses
strings.
A valid parentheses string s is primitive if it is nonempty, and there does not
exist a way to split it into s = A + B, with A and B nonempty valid parentheses
strings.
Given a valid parentheses string s, consider its primitive decomposition: s =
P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in
the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" +
"(())".
After removing outer parentheses of each part, this is "()()" + "()" =
"()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())"
+ "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())"
= "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Constraints:
1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        S = []

        L = R = i = j = 0
        n = len(s)

        while j < n:
            if s[j] == "(":
                L += 1
            else:
                R += 1

            if L == R:
                S += s[i + 1:  j]
                i = j + 1
            j += 1

        return "".join(S)


if __name__ == '__main__':
    sol = Solution()
    assert sol.removeOuterParentheses(s="(()())(())") == "()()()"
    assert sol.removeOuterParentheses(s="(()())(())(()(()))") == "()()()()(())"
    assert sol.removeOuterParentheses(s="()()") == ""

"""
Given a string expression representing an expression of fraction addition and
subtraction, return the calculation result in string format.
The final result should be an irreducible fraction. If your final result is an
integer, change it to the format of a fraction that has a denominator 1. So in
this case, 2 should be converted to 2/1.

Example 1:
Input: expression = "-1/2+1/2"
Output: "0/1"

Example 2:
Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Example 3:
Input: expression = "1/3-1/2"
Output: "-1/6"

Constraints:
The input string only contains '0' to '9', '/', '+' and '-'. So does the
output.
Each fraction (input and output) has the format ±numerator/denominator. If the
first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and
denominator of each fraction will always be in the range [1, 10]. If the
denominator is 1, it means this fraction is actually an integer in a fraction
format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid
and in the range of 32-bit int.
"""

import math
from re import findall
from typing import List


class Solution:
    def _find_pattern(self, rgx: str, expression: str) -> List[int]:
        return list(map(int, findall(rgx, expression)))

    def fractionAddition(self, expression: str) -> str:
        numerators = self._find_pattern(r"-?\d+(?=/)", expression)
        denominators = self._find_pattern(r"(?<=/)\d+", expression)
        max_denominator = math.lcm(*denominators)
        total_numerator = int(sum(
            max_denominator / d * n for n, d in zip(numerators, denominators)
        ))
        gcd = math.gcd(max_denominator, total_numerator)

        return f"{total_numerator // gcd}/{max_denominator // gcd}"


if __name__ == '__main__':
    sol = Solution()
    assert sol.fractionAddition(expression="-1/2+1/2") == "0/1"
    assert sol.fractionAddition(expression="-1/2+1/2+1/3") == "1/3"
    assert sol.fractionAddition(expression="1/3-1/2") == "-1/6"

    assert sol.fractionAddition(expression="-5/2+10/3+7/9") == "29/18"

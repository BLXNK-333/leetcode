"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e,
i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before
s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045

Constraints:
1 <= n <= 50 
"""

from math import factorial


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # f = int(factorial(n + 4) / (factorial(4) * factorial(n)))

        def rec(i: int = 0, counter: int = 0):
            if counter == n:
                return 1
            res = 0
            for j in range(i, 5):
                res += rec(j, counter + 1)
            return res

        return rec()


if __name__ == '__main__':
    obj = Solution()

    print(obj.countVowelStrings(33))

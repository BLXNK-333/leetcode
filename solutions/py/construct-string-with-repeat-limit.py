"""
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString
using the characters of s such that no letter appears more than repeatLimit times in a row. You
do not have to use all characters from s.
Return the lexicographically largest repeatLimitedString possible.
A string a is lexicographically larger than a string b if in the first position where a and b
differ, string a has a letter that appears later in the alphabet than the corresponding letter
in b. If the first min(a.length, b.length) characters do not differ, then the longer string is
the lexicographically larger one.

Example 1:
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid
repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than
3 times in a row, so it is not a valid repeatLimitedString.

Example 2:
Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString
"bbabaa".
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid
repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than
2 times in a row, so it is not a valid repeatLimitedString.

Constraints:
1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.
"""

import heapq


class Solution:
    def counter(self, s: str) -> list:
        d = {}
        for letter in s:
            d[ord(letter)] = d.get(ord(letter), 0) + 1
        return [[-k, v] for k, v in d.items()]

    def get_first(self, H) -> list:
        res = []
        letter, amount = heapq.heappop(H)
        res.append([letter, 1])
        if amount - 1 > 0:
            heapq.heappush(H, [letter, amount - 1])
        return res

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        H = self.counter(s)
        heapq.heapify(H)
        result = self.get_first(H)
        temp = []
        while H:
            letter, amount = heapq.heappop(H)
            if result[-1][0] != letter:
                result.append([letter, 1])
                if amount - 1 > 0:
                    heapq.heappush(H, [letter, amount - 1])
                for item in temp:
                    heapq.heappush(H, item)
                temp = []
            elif result[-1][0] == letter and result[-1][1] < repeatLimit:
                result.append([letter, result[-1][1] + 1])
                if amount - 1 > 0:
                    heapq.heappush(H, [letter, amount - 1])
                for item in temp:
                    heapq.heappush(H, item)
                temp = []
            else:
                temp.append([letter, amount])
        return "".join([chr(abs(letter)) for letter, _ in result])


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatLimitedString("cczazcc", 3))
    print(sol.repeatLimitedString("aababab", 2))
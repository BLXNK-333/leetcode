"""
Given a string array words, return an array of all characters that show up in all strings within
the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        S = Counter(words[0])
        for i in range(1, len(words)):
            S &= Counter(words[i])
        for letter, repeat in S.items():
            result.extend([letter] * repeat)
        return result


if __name__ == '__main__':
    obj = Solution()
    print(obj.commonChars(["bella", "label", "roller"]))
    print(obj.commonChars(["cool", "lock", "cook"]))

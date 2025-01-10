"""
You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including
multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a
subset of a.
Return an array of all the universal strings in words1. You may return the
answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
["l","e"]
Output: ["apple","google","leetcode"]

Constraints:
1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""

from typing import List, Dict


class Solution:
    def _compare_freq(self, scheme: Dict[str, int], target: Dict[str, int]) -> bool:
        for k, v in scheme.items():
            if k not in target or v > target[k]:
                return False
        return True

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []
        scheme = {}
        for word in words2:
            w2_map = {}
            for letter in word:
                w2_map[letter] = w2_map.get(letter, 0) + 1
            for k, v in w2_map.items():
                scheme[k] = max(scheme.get(k, 0), v)

        for word in words1:
            target_word = {}
            for letter in word:
                target_word[letter] = target_word.get(letter, 0) + 1

            if self._compare_freq(scheme, target_word):
                result.append(word)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"],
        words2=["e", "o"])
    )
    print(sol.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"],
        words2=["lo", "eo"]
    ))

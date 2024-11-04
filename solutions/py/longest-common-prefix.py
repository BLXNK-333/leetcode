"""
Write a function to find the longest common prefix string amongst an array of
strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)

        for word in strs:
            if not prefix:
                break

            for i, ltr in enumerate(prefix):
                if ltr != word[i]:
                    prefix = prefix[:i]
                    break
        return prefix


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(strs=["flower", "flow", "flight"]))

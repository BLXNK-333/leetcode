"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and
end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.

Example 1:
Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.

Example 2:
Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.

Example 3:
Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".

Constraints:
1 <= s.length <= 1000
s contains lowercase English letters only.
"""

from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        i, counter = 0, 1
        for j in range(1, len(s)):
            if s[j] == s[i]:
                counter += 1
            else:
                if counter > 2:
                    result.append([i, j - 1])
                counter = 1
                i = j
        if counter > 2:
            result.append([i, len(s) - 1])
        return result


if __name__ == '__main__':
    obj = Solution()
    assert obj.largeGroupPositions("abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]]
    assert obj.largeGroupPositions("aaa") == [[0, 2]]

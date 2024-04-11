"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is
secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai
trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a
trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1
otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:
1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            return -1

        one_who_trusts = set()
        one_who_is_trusted = {}

        for a, b in trust:
            one_who_trusts.add(a)
            one_who_is_trusted[b] = one_who_is_trusted.get(b, 0) + 1

        if len(one_who_trusts) != n - 1:
            return -1

        for k, v in one_who_is_trusted.items():
            if v == n - 1 and k not in one_who_trusts:
                return k
        return -1


if __name__ == '__main__':
    obj = Solution()

    assert obj.findJudge(n=2, trust=[[1, 2]]) == 2
    assert obj.findJudge(n=3, trust=[[1, 3], [2, 3]]) == 3
    assert obj.findJudge(n=2, trust=[[1, 3], [2, 3], [3, 1]]) == -1
    assert obj.findJudge(n=2, trust=[]) == -1
    assert obj.findJudge(n=4, trust=[[1, 2], [1, 3], [2, 1], [2, 3], [1, 4], [4, 3], [4, 1]]) == 3

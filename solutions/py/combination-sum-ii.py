"""
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

from typing import List, Optional


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)

        def dfs(comb: Optional[List[int]] = None, summ: int = 0, i: int = 0):
            if comb is None:
                comb = []

            if summ == target:
                result.append(comb[:])
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                next_summ = summ + candidates[j]
                if next_summ > target:
                    break

                comb.append(candidates[j])
                dfs(comb, next_summ, j + 1)
                comb.pop()

        dfs()
        return result


if __name__ == '__main__':
    sol = Solution()
    print(*sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8), sep="\n")


"""
Given two strings s and goal, return true if and only if s can become goal after some number of
shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Constraints:
1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
"""

from collections import deque


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        deq = deque(s)
        for _ in range(len(s)):
            deq.append(deq.popleft())
            for i in range(len(goal)):
                if deq[i] != goal[i]:
                    break
            else:
                return True
        return False


if __name__ == '__main__':
    obj = Solution()
    s = "xueta_podzalupnaya"
    goal = "axueta_podzalupnay"
    print(obj.rotateString(s, goal))

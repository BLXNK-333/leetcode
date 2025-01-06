"""
You have n boxes. You are given a binary string boxes of length n, where
boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
In one operation, you can move one ball from a box to an adjacent box. Box i is
adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be
more than one ball in some boxes.
Return an array answer of size n, where answer[i] is the minimum number of
operations needed to move all the balls to the ith box.
Each answer[i] is calculated considering the initial state of the boxes.

Example 1:
Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first
box in one operation.
2) Second box: you will have to move one ball from the first box to the second
box in one operation.
3) Third box: you will have to move one ball from the first box to the third
box in two operations, and move one ball from the second box to the third box
in one operation.

Example 2:
Input: boxes = "001011"
Output: [11,8,5,4,3,4]

Constraints:
n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.
"""

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Output: [11, 8, 5, 4, 3, 4]
        # Input: boxes = "001011"
        # _LEFT = [[0, 0], [0, 0], [1, 0], [1, 1], [2, 2], [3, 4]]
        # RIGHT = [[3, 11], [3, 8], [3, 5], [2, 3], [2, 1], [1, 0]]
        # TOTAL = [11, 8, 5, 4, 3, 4]

        n = len(boxes)
        LEFT = [[0, 0] for _ in range(n)]
        RIGHT = [[0, 0] for _ in range(n)]

        for i in range(n):
            prev = LEFT[max(i - 1, 0)]
            LEFT[i][1] = sum(prev)
            LEFT[i][0] = prev[0] + int(boxes[i] == "1")

        m = n - 1
        for i in range(m, -1, -1):
            prev = RIGHT[min(i + 1, m)]
            RIGHT[i][1] = sum(prev)
            RIGHT[i][0] = prev[0] + int(boxes[i] == "1")

        TOTAL = [LEFT[i][1] + RIGHT[i][1] for i in range(n)]
        return TOTAL


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations(boxes="110"))
    print(sol.minOperations(boxes="001011"))

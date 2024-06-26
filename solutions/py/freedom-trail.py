"""
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial
called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.
Given a string ring that represents the code engraved on the outer ring and another string key
that represents the keyword that needs to be spelled, return the minimum number of steps to
spell all the characters in the keyword.
Initially, the first character of the ring is aligned at the "12:00" direction. You should spell
all the characters in key one by one by rotating ring clockwise or anticlockwise to make each
character of the string key aligned at the "12:00" direction and then by pressing the center
button.
At the stage of rotating the ring to spell the key character key[i]:
You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The
final purpose of the rotation is to align one of ring's characters at the "12:00" direction,
where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to
spell, which also counts as one step. After the pressing, you could begin to spell the next
character in the key (next stage). Otherwise, you have finished all the spelling.

Example 1:
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this
character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two
steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.

Example 2:
Input: ring = "godding", key = "godding"
Output: 13

Constraints:
1 <= ring.length, key.length <= 100
ring and key consist of only lower case English letters.
It is guaranteed that key could always be spelled by rotating ring.
"""

from collections import defaultdict


class Solution:
    def get_graph(self, ring: str) -> dict:
        graph = defaultdict(list)
        for i, val in enumerate(ring):
            graph[val].append(i)
        return graph

    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        graph = self.get_graph(ring)

        dp = [[float('inf')] * n for _ in range(len(key))]

        for i in graph[key[0]]:
            dp[0][i] = min(i, n - i) + 1

        for i in range(1, len(key)):
            for j in graph[key[i]]:
                for k in graph[key[i - 1]]:
                    x1 = abs(j - k)
                    x2 = n - x1
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(x1, x2) + 1)

        return int(min(dp[-1]))


if __name__ == '__main__':
    sol = Solution()
    assert sol.findRotateSteps(ring="axbccyxb", key="abc") == 6
    assert sol.findRotateSteps(ring="caotmcaataijjxi", key="oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx") == 137

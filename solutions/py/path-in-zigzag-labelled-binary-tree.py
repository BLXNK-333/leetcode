"""
In an infinite binary tree where every node has two children, the nodes are labelled in row
order.
In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right,
while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
Given the label of a node in this tree, return the labels in the path from the root of the tree
to the node with that label.

Example 1:
Input: label = 14
Output: [1,3,4,14]

Example 2:
Input: label = 26
Output: [1,2,6,10,26]

Constraints:
1 <= label <= 10^6
"""

from typing import List


class Solution:
    def get_level(self, label: int) -> int:
        x, level = 2, 1
        while x - 1 < label:
            x *= 2
            level += 1
        return level

    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        array = []
        level = self.get_level(label)
        start = label
        if not level % 2:
            a, b = 2 ** (level - 1), 2 ** level - 1
            label = a + (b - label)

        while label > 1:
            a, b = 2 ** (level - 1), 2 ** level - 1
            if level % 2:
                array.append(label)
            else:
                current = a + (b - label)
                array.append(current)
            label //= 2
            level -= 1

        array[0] = start
        array.append(1)
        return array[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.pathInZigZagTree(14))
    print(sol.pathInZigZagTree(26))
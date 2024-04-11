"""
Given the root of a binary tree, return an array of the largest value in each row of the tree
(0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def rec(node, level: int = 0):
            if node:
                if len(result) == level:
                    result.append(node.val)
                else:
                    result[level] = max(result[level], node.val)
                rec(node.left, level + 1)
                rec(node.right, level + 1)

        rec(root)
        return result

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around
its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
Follow up: Could you solve it both recursively and iteratively?
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        L, R = {}, {}

        def dfs(node, mapp: dict, level=0):
            if node is None:
                mapp[level] = mapp.get(level, []) + [None]
                return
            dfs(node.left, mapp, level + 1)
            dfs(node.right, mapp, level + 1)
            mapp[level] = mapp.get(level, []) + [node.val]

        dfs(root.left, L)
        dfs(root.right, R)

        for key, val in L.items():
            if key not in R:
                return False
            if val != R[key][::-1]:
                return False
        return True


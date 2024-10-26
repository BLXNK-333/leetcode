"""
For a binary tree T, we can define a flip operation as follows: choose any
node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can
make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two
trees are flip equivalent or false otherwise.

Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
[1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Constraints:
The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(r1, r2):
            if not r1 and not r2:
                return True

            if not r1 or not r2 or r1.val != r2.val:
                return False

            return (dfs(r1.left, r2.left) and dfs(r1.right, r2.right)) or \
                    (dfs(r1.left, r2.right) and dfs(r1.right, r2.left))

        return dfs(root1, root2)

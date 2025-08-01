"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's
descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _tree_to_row(self, node):
        arr = []

        def dfs(node):
            if node is None:
                arr.append("N")
                return
            arr.append(f"~{node.val}~")
            dfs(node.left)
            dfs(node.right)

        dfs(node)
        return ",".join(arr)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        orig = self._tree_to_row(root)
        sub = self._tree_to_row(subRoot)
        return sub in orig



if __name__ == '__main__':
    ROOT = TreeNode(1)
    ROOT.left = TreeNode(1)

    SUB = TreeNode(1)
    sol = Solution()
    print(sol.isSubtree(ROOT, SUB))

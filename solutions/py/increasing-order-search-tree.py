"""
Given the root of a binary search tree, rearrange the tree in in-order so that
the leftmost node in the tree is now the root of the tree, and every node has
no left child and only one right child.

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]

Constraints:
The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        S = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            S.append(node)
            dfs(node.right)

        dfs(root)
        S.append(None)

        for i in range(len(S) - 1):
            cur = S[i]
            nex = S[i + 1]
            cur.left = None
            cur.right = nex

        return S[0]


if __name__ == '__main__':
    # [5,3,6,2,4,null,8,1,null,null,null,7,9]
    ROOT = TreeNode(5)
    ROOT.left = TreeNode(3)
    ROOT.right = TreeNode(6)
    ROOT.left.left = TreeNode(2)
    ROOT.left.right = TreeNode(4)
    ROOT.left.left.left = TreeNode(1)
    ROOT.right.right = TreeNode(8)
    ROOT.right.right.left = TreeNode(7)
    ROOT.right.right.right = TreeNode(9)

    sol = Solution()
    sol.increasingBST(ROOT)

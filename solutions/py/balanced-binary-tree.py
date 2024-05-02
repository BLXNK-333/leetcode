"""
Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node, depth=0):
            nonlocal res
            if res:
                if node is None:
                    return depth
                L = dfs(node.left, depth + 1)
                R = dfs(node.right, depth + 1)
                try:
                    M = abs(L - R)
                    if M > 1:
                        res = False
                        return
                except TypeError:
                    res = False
                    return
                return max(L, R)
        dfs(root)
        return res


if __name__ == '__main__':
    N = TreeNode(3)
    N.left = TreeNode(9)
    N.right = TreeNode(20)
    N.right.left = TreeNode(15)
    N.right.right = TreeNode(7)

    sol = Solution()
    print(sol.isBalanced(N))

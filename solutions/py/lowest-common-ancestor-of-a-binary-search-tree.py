"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of
itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        branches = []

        def dfs(node, branch: list):
            if node is None or len(branches) == 2:
                return
            branch = branch + [node]
            if node is p or node is q:
                branches.append(branch)
            dfs(node.left, branch)
            dfs(node.right, branch)

        dfs(root, [])

        b1, b2 = branches
        i, n, m = 0, len(b1), len(b2)
        prev = b1[0]

        while i < n and i < m and b1[i] == b2[i]:
            prev = b1[i]
            i += 1
        return prev


if __name__ == '__main__':
    ROOT = TreeNode(1)
    P = ROOT.left = TreeNode(2)
    Q = ROOT.right = TreeNode(3)

    sol = Solution()
    result = sol.lowestCommonAncestor(ROOT, P, Q)
    assert result == ROOT

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
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

        def dfs(node, target, path=None):
            if path is None:
                path = []
            if node is None:
                return

            path.append(node)
            if node is target:
                return path[:]

            L = dfs(node.left, target, path)
            if L:
                return L

            R = dfs(node.right, target, path)
            if R:
                return R

            path.pop()

        P = dfs(root, p)
        Q = dfs(root, q)
        i = -1
        for a, b in zip(P, Q):
            if a is not b:
                break
            i += 1
        return P[max(i, 0)]


if __name__ == '__main__':
    # root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    ROOT = TreeNode(3)
    ROOT.left = TreeNode(5)
    ROOT.right = TreeNode(1)
    ROOT.left.left = TreeNode(6)
    ROOT.left.right = TreeNode(2)
    ROOT.left.right.left = TreeNode(7)
    ROOT.left.right.right = TreeNode(4)
    ROOT.right.left = TreeNode(0)
    ROOT.right.right = TreeNode(8)

    sol = Solution()
    print(sol.lowestCommonAncestor(ROOT, ROOT.left, ROOT.left.right.right).val)

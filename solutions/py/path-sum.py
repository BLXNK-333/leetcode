"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-
leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        result = False

        def dfs(node, reduce=0):
            nonlocal result
            reduce += node.val
            if node.left is None and node.right is None:
                if reduce == targetSum:
                    result = True
                return
            if node.left:
                dfs(node.left, reduce)
            if node.right:
                dfs(node.right, reduce)

        dfs(root)
        return result


if __name__ == '__main__':
    sol = Solution()

    N = TreeNode(1)
    N.left = TreeNode(2)
    N.right = TreeNode(3)
    print(sol.hasPathSum(N, 5))
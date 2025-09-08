"""
You are given the root of a binary tree where each node has a value 0 or 1.
Each root-to-leaf path represents a binary number starting with the most
significant bit.
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from
the root to that leaf. Return the sum of these numbers.
The test cases are generated so that the answer fits in a 32-bits integer.

Example 1:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:
Input: root = [0]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        total = 0
        comb = []

        def dfs(node):
            comb.append(str(node.val))

            if node.left is None and node.right is None:
                nonlocal total
                total += int("".join(comb), 2)
                return

            if node.left:
                dfs(node.left)
                comb.pop()
            if node.right:
                dfs(node.right)
                comb.pop()

        dfs(root)
        return total


if __name__ == "__main__":
    sol = Solution()

    ROOT = TreeNode(1)
    ROOT.left = TreeNode(0)
    ROOT.right = TreeNode(1)

    ROOT.left.left = TreeNode(0)
    ROOT.left.right = TreeNode(1)
    ROOT.right.left = TreeNode(0)
    ROOT.right.right = TreeNode(1)

    print(sol.sumRootToLeaf(ROOT))

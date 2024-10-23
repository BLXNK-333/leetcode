"""
Given the root of a binary tree, replace the value of each node in the tree
with the sum of all its cousins' values.
Two nodes of a binary tree are cousins if they have the same depth with
different parents.
Return the root of the modified tree.
Note that the depth of a node is the number of edges in the path from the root
node to it.

Example 1:
Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary
tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.

Example 2:
Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary
tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = {}

        def dfs_preview(node, depth=0):
            sum_children = 0
            next_depth = depth + 1

            if node.left:
                sum_children += node.left.val
                dfs_preview(node.left, next_depth)

            if node.right:
                sum_children += node.right.val
                dfs_preview(node.right, next_depth)

            total[depth] = total.get(depth, 0) + sum_children

        dfs_preview(root)

        def dfs_insert(node, depth=0):
            next_depth = depth + 1
            sum_children = 0
            if node.left:
                sum_children += node.left.val
            if node.right:
                sum_children += node.right.val

            if node.left:
                if next_depth < 2:
                    node.left.val = 0
                else:
                    node.left.val = total[depth] - sum_children

                dfs_insert(node.left, next_depth)

            if node.right:
                if next_depth < 2:
                    node.right.val = 0
                else:
                    node.right.val = total[depth] - sum_children

                dfs_insert(node.right, next_depth)

        root.val = 0
        dfs_insert(root)
        return root


if __name__ == '__main__':
    ROOT = TreeNode(5)
    ROOT.left = TreeNode(4)
    ROOT.right = TreeNode(9)
    ROOT.left.left = TreeNode(1)
    ROOT.left.right = TreeNode(10)
    ROOT.right.right = TreeNode(7)

    sol = Solution()
    print(sol.replaceValueInTree(ROOT))

    print(ROOT.val)
    print(ROOT.left.val)
    print(ROOT.right.val)
    print(ROOT.left.left.val)
    print(ROOT.left.right.val)
    print(ROOT.right.right.val)


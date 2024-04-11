"""
A binary tree is named Even-Odd if it meets the following conditions:
The root of the binary tree is at level index 0, its children are at level index 1, their
children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly
increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly
decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return
false.

Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing,
the tree is Even-Odd.

Example 2:
Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:
Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 106
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level, queue, temp = 0, [root], []

        def append_child(node):
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

        while queue:
            x = level & 1
            if queue[0].val & 1 == x:
                return False
            append_child(queue[0])
            if len(queue) > 1:
                if x:
                    for i in range(1, len(queue)):
                        if queue[i].val >= queue[i - 1].val or queue[i].val & 1:
                            return False
                        append_child(queue[i])
                else:
                    for i in range(1, len(queue)):
                        if queue[i].val <= queue[i - 1].val or not queue[i].val & 1:
                            return False
                        append_child(queue[i])
            queue = temp
            temp = []
            level += 1
        return True


if __name__ == '__main__':
    # [1,10,4,3,null,7,9,12,8,6,null,null,2]
    ROOT = TreeNode(1)
    ROOT.left = TreeNode(10)
    ROOT.right = TreeNode(4)
    ROOT.left.left = TreeNode(3)
    ROOT.right.left = TreeNode(7)
    ROOT.right.right = TreeNode(9)
    ROOT.left.left.left = TreeNode(12)
    ROOT.left.left.right = TreeNode(8)
    ROOT.right.left.left = TreeNode(6)
    ROOT.right.right.right = TreeNode(2)

    # [5,9,1,3,5,7]
    ROOT2 = TreeNode(5)
    ROOT2.left = TreeNode(9)
    ROOT2.right = TreeNode(1)
    ROOT2.left.left = TreeNode(3)
    ROOT2.left.right = TreeNode(5)
    ROOT2.right.left = TreeNode(7)

    # [15, 26, 1]
    ROOT3 = TreeNode(15)
    ROOT3.left = TreeNode(26)
    ROOT3.right = TreeNode(1)

    sol = Solution()
    assert sol.isEvenOddTree(ROOT) is True
    assert sol.isEvenOddTree(ROOT2) is False
    assert sol.isEvenOddTree(ROOT3) is False

"""
Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should
populate each next pointer to point to its next right node, just like in Figure
B. The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not
count as extra space for this problem.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def dfs(cur_node, depth=0, branch=None):
            if cur_node is None:
                return

            levels_last_node = branch.get(depth)
            if levels_last_node:
                levels_last_node.next = cur_node
            branch[depth] = cur_node

            new_depth = depth + 1
            dfs(cur_node.left, new_depth, branch)
            dfs(cur_node.right, new_depth, branch)

        dfs(root, 0, {})
        return root





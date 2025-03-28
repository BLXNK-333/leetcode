"""
Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
Note: This question is the same as 783: https://leetcode.com/problems/minimum-
distance-between-bst-nodes/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        min_val = 10 ** 6

        def dfs(node):
            if node is None:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        arr.sort()

        for i in range(1, len(arr)):
            x = arr[i] - arr[i - 1]
            if x < min_val:
                min_val = x
        return min_val




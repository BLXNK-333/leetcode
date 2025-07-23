"""
Given the head of a singly linked list where elements are sorted in ascending
order, convert it to a height-balanced binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
shown height balanced BST.

Example 2:
Input: head = []
Output: []

Constraints:
The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_array(self, head: Optional[ListNode]) -> List[int]:
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        return lst

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        array = self.get_array(head)

        def dfs(L, R):
            if L + 1 >= R:
                return None
            else:
                M = (L + R) // 2
                node = TreeNode(array[M])

            node.left = dfs(L, M)
            node.right = dfs(M, R)

            return node

        return dfs(-1, len(array))

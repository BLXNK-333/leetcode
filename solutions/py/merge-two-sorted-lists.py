"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes
of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list2
        if not list1:
            return list2
        if not list2:
            return list1

        start_node = ListNode()
        next_node = ListNode()
        start_node.next = next_node

        i, j = list1, list2

        while i and j:
            if i.val <= j.val:
                next_node.next = i
                next_node = i
                i = i.next
            else:
                next_node.next = j
                next_node = j
                j = j.next

        if i:
            next_node.next = i
        elif j:
            next_node.next = j
        return start_node.next.next

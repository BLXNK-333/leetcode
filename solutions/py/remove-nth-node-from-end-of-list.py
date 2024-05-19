"""
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
Follow up: Could you do this in one pass?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        array = []

        cur_node = head
        i = 0
        while cur_node:
            array.append((i, cur_node))
            cur_node = cur_node.next
            i += 1

        target = len(array) - n
        if len(array) == 1:
            return None
        if target == len(array):
            array[-2][1].next = None
            return head
        if target == 0:
            return array[1][1]

        prev = array[target - 1][1]
        cur = array[target][1]
        prev.next = cur.next
        return head




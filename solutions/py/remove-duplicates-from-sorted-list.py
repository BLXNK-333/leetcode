"""
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        nexxt = cur.next
        while nexxt:
            if nexxt.val != cur.val:
                cur.next = nexxt
                cur = nexxt
            nexxt = nexxt.next

        cur.next = None

        return head


if __name__ == '__main__':
    ROOT = ListNode(1)
    ROOT.next = ListNode(1)
    ROOT.next.next = ListNode(2)
    ROOT.next.next.next = ListNode(3)
    ROOT.next.next.next.next = ListNode(3)

    sol = Solution()
    sol.deleteDuplicates(ROOT)

    while ROOT:
        print(ROOT.val, end=" ")
        ROOT = ROOT.next

"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        array = []
        while head:
            array.append(head)
            head = head.next

        if len(array) == 1:
            return array[0]

        i, j = 0, len(array) - 1
        new_list = []
        while i <= j:
            new_list.append(array[i])
            new_list.append(array[j])
            i += 1
            j -= 1

        for i in range(1, len(new_list)):
            new_list[i - 1].next = new_list[i]
        new_list[-1].next = None
        return new_list[0]
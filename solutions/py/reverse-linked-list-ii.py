"""
Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
Follow up: Could you do it in one pass?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int
                       ) -> Optional[ListNode]:
        A, L, R = [], left - 1, right - 1

        while head:
            A.append(head)
            head = head.next

        while L < R:
            A[L], A[R] = A[R], A[L]
            L += 1
            R -= 1

        n = len(A)
        for i in range(n - 1):
            A[i].next = A[i + 1]

        A[n - 1].next = None
        return A[0]

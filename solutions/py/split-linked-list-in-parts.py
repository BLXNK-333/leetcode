"""
Given the head of a singly linked list and an integer k, split the linked list
into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should
have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts
occurring earlier should always have a size greater than or equal to parts
occurring later.
Return an array of the k parts.

Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode
is [].

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.

Constraints:
The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_list_length(self, start: Optional[ListNode]) -> int:
        ln = 0
        while start is not None:
            ln += 1
            start = start.next
        return ln

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[
        Optional[ListNode]]:
        length = self.get_list_length(head)
        a, b = divmod(length, k)
        result = []

        for _ in range(k):
            part_length = a + 1 if b > 0 else a
            if part_length:
                result.append(head)
                for j in range(1, part_length + 1):
                    nexxt = head.next
                    if j == part_length:
                        head.next = None
                    head = nexxt
                b -= 1
            else:
                result.append(None)
        return result


if __name__ == '__main__':
    ROOT = CUR = ListNode(1)
    for i in range(2, 11):
        NEXT = ListNode(i)
        CUR.next = NEXT
        CUR = NEXT

    sol = Solution()
    print(sol.splitListToParts(ROOT, 3))

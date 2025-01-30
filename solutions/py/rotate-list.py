"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        array = []
        while head:
            array.append(head)
            head = head.next

        n = len(array)
        k %= n
        start_idx = n - k if k else 0

        array[n - 1].next = array[0]
        array[start_idx - 1].next = None
        return array[start_idx]


class TestSolution:
    def __init__(self):
        self.sol = Solution()

    def _check_func(self, head: Optional[ListNode]):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_with_5_nodes(self):
        HEAD = ListNode(1)
        HEAD.next = ListNode(2)
        HEAD.next.next = ListNode(3)
        HEAD.next.next.next = ListNode(4)
        HEAD.next.next.next.next = ListNode(5)

        new_head = self.sol.rotateRight(HEAD, 2)
        assert self._check_func(new_head) == [4, 5, 1, 2, 3]

    def test_with_1_node(self):
        HEAD = ListNode(1)
        new_head = self.sol.rotateRight(HEAD, 3)
        assert self._check_func(new_head) == [1]

    def test_with_empty_list(self):
        HEAD = None
        new_head = self.sol.rotateRight(HEAD, 4)
        assert self._check_func(new_head) == []

    def test_with_k_greater_than_length(self):
        HEAD = ListNode(1)
        HEAD.next = ListNode(2)
        HEAD.next.next = ListNode(3)

        new_head = self.sol.rotateRight(HEAD, 5)
        assert self._check_func(new_head) == [2, 3, 1]

    def test_with_k_zero(self):
        HEAD = ListNode(1)
        HEAD.next = ListNode(2)
        HEAD.next.next = ListNode(3)

        new_head = self.sol.rotateRight(HEAD, 0)
        assert self._check_func(new_head) == [1, 2, 3]


if __name__ == '__main__':
    test = TestSolution()
    test.test_with_5_nodes()
    test.test_with_1_node()
    test.test_with_empty_list()
    test.test_with_k_greater_than_length()
    test.test_with_k_zero()

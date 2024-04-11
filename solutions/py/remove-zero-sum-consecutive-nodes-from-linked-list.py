"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to
0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.
(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def convet_to_array(self, node):
        array = []
        while node:
            array.append(node.val)
            node = node.next
        return array

    def convert_to_list(self, array: list):
        start_node = cur_node = ListNode(array[0])
        next_node = None
        for i in range(1, len(array)):
            next_node = ListNode(array[i])
            cur_node.next = next_node
            cur_node = next_node
        return start_node

    def remove_seq(self, array: list):
        for i in range(len(array) - 1):
            s = array[i]
            for j in range(i + 1, len(array)):
                s += array[j]
                if not s:
                    return array[:i] + array[j + 1:]

    def remove_nulls(self, array: list):
        return [i for i in array if i]

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = self.remove_nulls(self.convet_to_array(head))
        if not array:
            return None
        while True:
            new_array = self.remove_seq(array)
            if new_array is None:
                return self.convert_to_list(array)
            if not new_array:
                return None
            array = new_array


if __name__ == "__main__":
    obj = Solution()
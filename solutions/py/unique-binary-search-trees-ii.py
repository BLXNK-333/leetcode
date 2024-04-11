"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has
exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8
"""

from typing import List, Optional
from itertools import permutations


def get_length(number: int) -> int:
    x = 1
    while number:
        x <<= 1
        number -= 1
    return x - 1


def get_tree(arr: tuple, length: int) -> tuple:
    tree = [0] * length
    tree[0] = arr[0]
    for i in range(1, len(arr)):
        j = 0
        while tree[j]:
            j = (j << 1) + (1 if tree[j] > arr[i] else 2)
        tree[j] = arr[i]
    return tuple(tree)


def get_all_struct(n: int):
    array = list(range(1, n + 1))
    length = get_length(len(array))
    result = set()
    for perm in permutations(array):
        result.add(get_tree(perm, length))
    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        array = get_all_struct(n)
        result = []

        def rec(node, strct: tuple = None, index: int = 0):
            left = index * 2 + 1
            right = index * 2 + 2
            if right > len(strct) or not strct[left] and not strct[right]:
                return
            if strct[left]:
                node.left = TreeNode(strct[left])
                rec(node.left, strct, left)

            if strct[right]:
                node.right = TreeNode(strct[right])
                rec(node.right, strct, right)

        for struct in array:
            root = TreeNode(struct[0])
            result.append(root)
            rec(root, struct)

        return result


if __name__ == '__main__':
    # O(n!) - bad practice
    sol = Solution()
    sol.generateTrees(3)
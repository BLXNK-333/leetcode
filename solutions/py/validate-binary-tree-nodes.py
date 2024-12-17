"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two
children leftChild[i] and rightChild[i], return true if and only if all the
given nodes form exactly one valid binary tree.
If node i has no left child then leftChild[i] will equal -1, similarly for the
right child.
Note that the nodes have no values and that we only use the node numbers in
this problem.

Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Constraints:
n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1
"""

from typing import List


class Solution:
    def find_potential_root(self, n: int, left: List[int], right: List[int]) -> int:
        hs = set(left) | set(right)
        for i in range(n):
            if i not in hs:
                return i
        return -1

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
                                rightChild: List[int]) -> bool:

        root = self.find_potential_root(n, leftChild, rightChild)
        if root == -1:
            return False
        queue = [(root, leftChild[root], rightChild[root])]
        visited = set()

        while queue:
            cur, L, R = queue.pop()
            if cur in visited:
                return False
            visited.add(cur)

            if L != -1:
                queue.append((L, leftChild[L], rightChild[L]))
            if R != -1:
                queue.append((R, leftChild[R], rightChild[R]))

        return len(visited) == n


if __name__ == '__main__':
    sol = Solution()
    assert sol.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1],
                                       rightChild=[2, -1, -1, -1]) == True
    assert sol.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1],
                                       rightChild=[2, 3, -1, -1]) == False
    assert sol.validateBinaryTreeNodes(n=4, leftChild=[3, -1, 1, -1],
                                       rightChild=[-1, -1, 0, -1]) == True
    assert sol.validateBinaryTreeNodes(n=4, leftChild=[1, 0, 3, -1],
                                       rightChild=[-1, -1, -1, -1]) == False

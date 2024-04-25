"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at
nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other
words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that
you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0
to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        inf = float("inf")
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0

        for i in range(n - 1):
            max_jump = i + nums[i]
            for j in range(i, min(max_jump + 1, n)):
                if dp[i] + 1 < dp[j]:
                    dp[j] = dp[i] + 1
        return int(dp[-1])


def wf():
    with open("/home/blxnk/Downloads/111.txt", "r") as file:
        res = file.readline()
        res = res.strip("[]\n").split(",")
        res = list(map(int, res))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.jump(nums=[1, 2, 1, 1, 1]))

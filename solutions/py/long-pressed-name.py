"""
Your friend is typing his name into a keyboard. Sometimes, when typing a
character c, the key might get long pressed, and the character will be typed 1
or more times.
You examine the typed characters of the keyboard. Return True if it is possible
that it was your friends name, with some characters (possibly none) being long
pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed
output.

Constraints:
1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, n, t = 0, 0, len(name), len(typed)
        if n > t:
            return False

        while i < n and j < t:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        if i < n:
            return False

        for j in range(j, t):
            if typed[j] != typed[j - 1]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isLongPressedName(name="alex", typed="aaleex"))
    print(sol.isLongPressedName(name="alex", typed="aaleexa"))
    print(sol.isLongPressedName(name="vtkgn", typed="vttkgnn"))

"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes
"AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        i, j = 0, len(s) - 1
        hs = set("aeiou" + "aeiou".upper())

        while i < j:
            if arr[i] not in hs:
                i += 1

            elif arr[j] not in hs:
                j -= 1

            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        return "".join(arr)


if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseVowels(s = "IceCreAm") == "AceCreIm"
    assert sol.reverseVowels(s = "leetcode") == "leotcede"
"""
Return the number of distinct non-empty substrings of text that can be written as the
concatenation of some string with itself (i.e. it can be written as a + a where a is some
string).

Example 1:
Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".

Example 2:
Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".

Constraints:
1 <= text.length <= 2000
text has only lowercase English letters.
"""

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        hash_map = {}
        hash_set = set()

        for index, letter in enumerate(text):
            hash_map[letter] = hash_map.get(letter, []) + [index]

        if len(hash_map) == 1:
            return len(hash_map[text[0]]) // 2

        for current in range(1, len(text)):
            for candidate in hash_map.get(text[current], []):
                i, j = current, candidate
                while j < current and i < len(text) and text[i] == text[j]:
                    i += 1
                    j += 1
                if j == current:
                    hash_set.add(text[candidate: current])

        return len(hash_set) - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.distinctEchoSubstrings('abcabcabc'))
    assert sol.distinctEchoSubstrings('leetcodeleetcode') == 2
    assert sol.distinctEchoSubstrings('abcabcabc') == 3




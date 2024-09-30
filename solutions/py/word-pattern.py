"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        array = s.split()
        if len(array) != len(pattern):
            return False

        hm_letter, hm_word = {}, {}
        for letter, word in zip(pattern, array):
            if letter in hm_letter or word in hm_word:
                if (letter not in hm_letter or word not in hm_word or
                        hm_letter[letter] != word or hm_word[word] != letter):
                    return False
            else:
                hm_letter[letter] = word
                hm_word[word] = letter
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern(pattern="abba", s="dog cat cat dog"))

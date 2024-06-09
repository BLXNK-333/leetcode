"""
Given an array of strings words, return the words that can be typed using
letters of the alphabet on only one row of American keyboard like the image
below.
In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
"""

from typing import List


class Solution:
    def __init__(self):
        self.s1 = set("qwertyuiop")
        self.s2 = set("asdfghjkl")
        self.s3 = set("zxcvbnm")

    def findWords(self, words: List[str]) -> List[str]:
        array = []
        for index, word in enumerate(words):
            key = word.lower()
            array.append((set(key), index))

        result = []
        for h_set, index in array:
            for seq in self.s1, self.s2, self.s3:
                candidate = h_set - seq
                if not len(candidate):
                    result.append(words[index])
                    break
                if len(candidate) != len(h_set):
                    break
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findWords(["asdfghjkla", "qwertyuiopq", "zxcvbnzzm",
                         "asdfghjkla", "qwertyuiopq", "zxcvbnzzm"]))

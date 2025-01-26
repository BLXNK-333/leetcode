"""
Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right)
justified.
You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line does not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is
inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters
only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."],
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth =
16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall
be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one
word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","e
xplain","to","a","computer.","Art","is","everything","else","we","do"],
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

from typing import List
from itertools import chain, zip_longest


class Solution:
    def _split_array(self, words: List[str], maxWidth: int) -> List[List[str]]:
        split_array = []
        cur_line = []
        i, cur_width, n = 0, 0, len(words)

        while i < n:
            cur_width += len(words[i])
            if cur_width <= maxWidth:
                cur_line.append(words[i])
                cur_width += 1
                i += 1
            else:
                split_array.append(cur_line)
                cur_width = 0
                cur_line = []

        if cur_line:
            split_array.append(cur_line)
        return split_array

    def _stretch_line_width(self, line: List[str], maxWidth: int) -> str:
        cnt_blanks = len(line) - 1
        len_words = sum(len(w) for w in line)
        if cnt_blanks:
            x, y = divmod((maxWidth - len_words), cnt_blanks)
            if x:
                fills = []
                while cnt_blanks:
                    if y:
                        fills.append(" " * (x + 1))
                        y -= 1
                    else:
                        fills.append(" " * x)
                    cnt_blanks -= 1

                res = "".join(chain(*zip_longest(line, fills, fillvalue="")))
                return res
        else:
            return line[0].ljust(maxWidth, " ")

    def _make_last_line(self, line: str, maxWidth: int) -> str:
        return " ".join(line.split()).ljust(maxWidth, " ")

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Input: words = ["Science","is","what","we","understand","well","enough","to","e
        xplain","to","a","computer.","Art","is","everything","else","we","do"],
        maxWidth = 20
        """
        split_arr = self._split_array(words, maxWidth)
        result = []
        for line in split_arr:
            result.append(self._stretch_line_width(line, maxWidth))
        if result:
            result[-1] = self._make_last_line(result[-1], maxWidth)
        return result


if __name__ == '__main__':
    sol = Solution()
    WORDS = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
             "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we",
             "do"]

    print(*sol.fullJustify(WORDS, 20), sep="\n")

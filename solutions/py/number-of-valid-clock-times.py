"""
You are given a string of length 5 called time, representing the current time
on a digital clock in the format "hh:mm". The earliest possible time is "00:00"
and the latest possible time is "23:59".
In the string time, the digits represented by the ? symbol are unknown, and
must be replaced with a digit from 0 to 9.
Return an integer answer, the number of valid clock times that can be created
by replacing every ? with a digit from 0 to 9.

Example 1:
Input: time = "?5:00"
Output: 2
Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or
"15:00". Note that we cannot replace it with a 2, since the time "25:00" is
invalid. In total, we have two choices.

Example 2:
Input: time = "0?:0?"
Output: 100
Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100
total choices.

Example 3:
Input: time = "??:??"
Output: 1440
Explanation: There are 24 possible choices for the hours, and 60 possible
choices for the minutes. In total, we have 24 * 60 = 1440 choices.

Constraints:
time is a valid string of length 5 in the format "hh:mm".
"00" <= hh <= "23"
"00" <= mm <= "59"
Some of the digits might be replaced with '?' and need to be replaced with
digits from 0 to 9.
"""


class Solution:
    def countTime(self, time: str) -> int:
        cnt = 1
        if time[0] == "?":
            if time[1] == "?":
                cnt *= 24
            elif time[1].isdigit() and int(time[1]) > 3:
                cnt *= 2
            else:
                cnt *= 3
        elif time[1] == "?":
            if time[0] == "2":
                cnt *= 4
            else:
                cnt *= 10
        if time[3] == "?":
            cnt *= 6
        if time[4] == "?":
            cnt *= 10

        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.countTime(time = "??:??"))

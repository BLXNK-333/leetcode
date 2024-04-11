"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you
and order one at a time (in the order specified by bills). Each customer will only buy one
lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each
customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if
you can provide every customer with the correct change, or false otherwise.

Example 1:
Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:
Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10
bills.
Since not every customer received the correct change, the answer is false.

Constraints:
1 <= bills.length <= 105
bills[i] is either 5, 10, or 20.
"""

from typing import List


class Solution:
    def get_change(self, client, amount):

        if client == 20 and amount['ten'] and amount['five']:
            amount['twenty'] += 1
            amount['ten'] -= 1
            amount['five'] -= 1
        elif client == 20 and amount['five'] >= 3:
            amount['twenty'] += 1
            amount['five'] -= 3
        elif client == 10 and amount['five']:
            amount['ten'] += 1
            amount['five'] -= 1
        else:
            return False
        return True

    def lemonadeChange(self, bills: List[int]) -> bool:
        amount = {'five': 0, 'ten': 0, 'twenty': 0}
        for client in bills:
            if client == 5:
                amount['five'] += 1
            elif (client == 10 or client == 20) and not self.get_change(client, amount):
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    assert obj.lemonadeChange([5, 5, 5, 10, 20]) is True
    assert obj.lemonadeChange([5, 5, 10, 10, 20]) is False

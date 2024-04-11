"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices
(1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a
product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the
prime number 5 is at index 1.

Example 2:
Input: n = 100
Output: 682289015

Constraints:
1 <= n <= 100
"""

class Solution:
    def get_sieve(self, n: int) -> list:
        result = list(range(n + 1))
        result[1] = 0
        for i in range(2, int(n ** .5 + 1)):
            if result[i]:
                for j in range(i * i, n + 1, i):
                    result[j] = 0
        return result

    def get_amount(self, array: list):
        p = c = 0
        for i in range(1, len(array)):
            if array[i]:
                p += 1
            else:
                c += 1
        return p, c

    def numPrimeArrangements(self, n: int) -> int:
        sieve = self.get_sieve(n)
        primes, composite = self.get_amount(sieve)
        result = 1
        for i in range(1, n + 1):
            if sieve[i]:
                result *= primes
                primes -= 1
            else:
                result *= composite
                composite -= 1

        return result % (10 ** 9 + 7)


if __name__ == '__main__':
    obj = Solution()
    print(obj.numPrimeArrangements(100))
    # 682289015
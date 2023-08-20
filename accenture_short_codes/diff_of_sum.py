"""
def differenceofSum(n. m)

The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.

Assumption:

n>0 and m>0
Sum lies between integral range
Example

Input
n:4
m:20
Output
90

Explanation

Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60
Sum of numbers not divisible by 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
Difference 150 – 60 = 90
Sample Input
n:3
m:10
Sample Output
19
"""


def get_biggest(n, m):
    low, high, result = 1, m, 1
    while low <= high:
        mid = low + (high - low) // 2
        if mid * n <= m:
            low = (result := mid) + 1
        else:
            high = mid - 1
    return result


def diff_of_sum(n, m):
    total_sum = (m * (m + 1)) // 2
    multiple = get_biggest(n, m)
    divisible_sum = ((multiple * (multiple + 1)) // 2) * n
    return abs(total_sum - (divisible_sum * 2))


n = int(input())
m = int(input())
print(diff_of_sum(n, m))

"""
You are required to implement the following function:
int Calculate(int m, int n);

The function accepts 2 positive integers ‘m’ and ‘n’ as its arguments.You are required to calculate the sum of numbers divisible both by 3 and 5, between ‘m’ and ‘n’ both inclusive and return the same.
Note
0 < m <= n

Example
Input:
m : 12
n : 50

Output
90

Explanation:
The numbers divisible by both 3 and 5, between 12 and 50 both inclusive are {15, 30, 45} and their sum is 90.

Sample Input
m : 100
n : 160

Sample Output
510
"""


def get_smallest_multiple_of_15(num):
    low, high, result = 1, num, 1
    while low <= high:
        mid = low + (high - low) // 2
        if mid * 15 >= num:
            high = (result := mid) - 1
        else:
            low = mid + 1
    return result


def divisible(m, n):
    multiple = get_smallest_multiple_of_15(m)
    return sum(range(multiple, (n // 15) + 1)) * 15


m = int(input())
n = int(input())
print(divisible(m, n))

"""
You are given a function,
int findCount(int arr[], int length, int num, int diff);

The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.

Example:
Input:

arr: 12 3 14 56 77 13
num: 13
diff: 2
Output:
3

Explanation:
Elements of ‘arr’ having absolute difference of less than or equal to ‘diff’ i.e. 2 with ‘num’ i.e. 13 are 12, 13 and 14.
"""


def ceiling(arr, key):
    low, high, result = 0, len(arr) - 1, len(arr)
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= key:
            high = (result := mid) - 1
        else:
            low = mid + 1
    return result


def floor(arr, key):
    low, high, result = 0, len(arr) - 1, -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= key:
            low = (result := mid) + 1
        else:
            high = mid - 1
    return result


def find_count(arr, num, diff):
    arr.sort()
    result = floor(arr, num + diff) - ceiling(arr, num - diff) + 1
    return result if result > 0 else -1


arr = [int(x) for x in input().split()]
num = int(input())
diff = int(input())
print(find_count(arr, num, diff))

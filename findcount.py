"""You are given a function,
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
Elements of ‘arr’ having absolute difference of less than or equal to ‘diff’ i.e. 2 with ‘num’ i.e. 13 are 12, 13 and 14."""
def findCount(arr, length, num, diff):
    count = 0
    
    for i in range(length):
        if abs(arr[i] - num) <= diff:
            count += 1
    
    if count > 0:
        return count
    else:
        return -1

# Test case
arr = list(map(int,input().split()))
num = int(input())
diff = int(input())
print(findCount(arr, len(arr), num, diff))  

###Output Example 
""" We are given an array arr with the elements [12, 3, 14, 56, 77, 13].
We are looking for elements in the array that have an absolute difference of less than or equal to 2 with the number 13.
Loop through each element in the array:
For the first element 12, the absolute difference with 13 is abs(12 - 13) = 1, which is less than or equal to 2.
For the second element 3, the absolute difference with 13 is abs(3 - 13) = 10, which is greater than 2.
For the third element 14, the absolute difference with 13 is abs(14 - 13) = 1, which is less than or equal to 2.
For the fourth element 56, the absolute difference with 13 is abs(56 - 13) = 43, which is greater than 2.
For the fifth element 77, the absolute difference with 13 is abs(77 - 13) = 64, which is greater than 2.
For the sixth element 13, the absolute difference with 13 is abs(13 - 13) = 0, which is less than or equal to 2.
Count the elements that satisfy the condition of having an absolute difference of less than or equal to 2 with the number 13. 
In this case, the elements [12, 13, 14] satisfy the condition.
The count of such elements is 3, so the function returns 3 as the output.
Therefore, the output of the function is 3, as there are three elements in the array that meet the criteria of having an absolute difference of less than or equal to 2 with the number 13. """"

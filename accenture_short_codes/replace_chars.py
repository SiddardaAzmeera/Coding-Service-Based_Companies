"""
Problem Statement

You are given a function,

Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

Assumption: String Contains only lower-case alphabetical letters.

Note:

Return null if string is null.
If both characters are not present in string or both of them are same , then return the string unchanged.
Example:

Input:
Str: apples
ch1:a
ch2:p
Output:
paales
Explanation:

‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales
"""


def replace_chars(string, ch1, ch2):
    result = ''
    for ch in string:
        if ch == ch1:
            result += ch2
        elif ch == ch2:
            result += ch1
        else:
            result += ch
    return result


string = input()
ch1 = input()
ch2 = input()
print(replace_chars(string, ch1, ch2))
""""Problem Statement

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

‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales"""
def replace_character(s, ch1, ch2):
    if s is None:
        return None
    
    if ch1 == ch2:
        return s
    
    modified_s = ""
    for char in s:
        if char == ch1:
            modified_s += ch2
        elif char == ch2:
            modified_s += ch1
        else:
            modified_s += char
    
    return modified_s

# Example usage
input_str = input()
ch1 = input()
ch2 = input()
result = replace_character(input_str, ch1, ch2)
print("Modified String:", result)

#Insights about the code 
"""def replace_character(s, ch1, ch2):

This line defines a function named replace_character that takes three parameters: s (the original string), ch1 (the character to replace), 
and ch2 (the replacement character).
if s is None:

This line checks if the input string s is None, indicating that the string is empty or not provided.
return None

If the input string s is None, this line returns None from the function, indicating that the input was invalid.
if ch1 == ch2:

This line checks if the characters ch1 and ch2 are the same.
return s

If ch1 and ch2 are the same, this line returns the original string s without any modifications.
modified_s = ""

This line initializes an empty string named modified_s, which will store the modified version of the input string.
for char in s:

This line starts a loop that iterates through each character (char) in the original string s.
if char == ch1:

This line checks if the current character char is equal to the character to be replaced, ch1.
modified_s += ch2

If the current character is equal to ch1, this line appends the replacement character ch2 to the modified_s string.
elif char == ch2:

This line checks if the current character char is equal to the replacement character, ch2.
modified_s += ch1

If the current character is equal to ch2, this line appends the original character ch1 to the modified_s string.
else:

If the current character is neither ch1 nor ch2, this line indicates that no replacement is needed.
modified_s += char

In this case, the current character is appended to the modified_s string as it is.
return modified_s

After the loop completes, this line returns the modified_s string, which contains the modified version of the input string.
Example usage:

This section demonstrates how to use the replace_character function.
input_str = "apples": Sets the original input string.
ch1 = 'a': Specifies the character to be replaced.
ch2 = 'p': Specifies the replacement character.
result = replace_character(input_str, ch1, ch2): Calls the function with the provided parameters.
print("Modified String:", result): Prints the modified string."""

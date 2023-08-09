""""Cut and Add
Harry and Potter took a word string. Harry chose a number M (less than the length of the
string) and Potter chose N (less than the length of the string). Harry will cut M alphabets
from the end of the string and then add it to the beginning and will give it to Potter. Then,
Potter will also cut N alphabets from the end of the string, add it to the beginning and ther
give to Harry. This process will continue till they get the original word string back.
For a given string and given values of M and N, find the number of turns in which they wi
get the original word string back.
Input Specification:
input1: Original word string
Value of M​ 
Example 1:
input1: AbcDef
input2: 1
input3: 2

output: 4
Explanation:
turn 1: fAbcDe
turn 2: DefAbc
turn 3:cDefAb
turn 4: AbcDef"""
def task(str1, M, N):
    strlst = list(str1)
    turns = 0
    while True:
        strlst = strlst[-M:] + strlst[:-M]
        turns += 1
        print(turns,"".join(strlst))
        if strlst == list(str1):
            break
        strlst = strlst[-N:] + strlst[:-N]
        turns += 1
        print(turns,"".join(strlst))
        if strlst == list(str1):
            break
    return turns
str1=input()
M=int(input())
N=int(input())
result=task(str1,M,N)
print(result)

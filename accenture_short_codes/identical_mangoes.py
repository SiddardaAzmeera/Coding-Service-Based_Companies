"""
Mango Distribution
Problem Statement
Given a number of mangoes and number of persons. Find the number of ways to distribute the identical mangoes among
identical persons.
Input Specification
input1: the number of mangoes
input2: the number of persons.
Output Specification
Return the number of ways to distribute identical mangoes among identical persons.
Sample Input/Output 1
Input
input1: 2
input2: 2
Output
Output: 3
Explanation
All possible distributions of 2 identical mangoes to 2 identical persons are (1, 1), (2, 0) and (0, 2). Hence the output is 3.
"""
from math import factorial


def distribute(mangoes, persons):
    return (factorial(mangoes + persons - 1) // (factorial(mangoes) * factorial(persons - 1)))


mangoes = int(input())
persons = int(input())
print(distribute(mangoes, persons))

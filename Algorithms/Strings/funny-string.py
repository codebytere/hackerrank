'''
Problem Statement
Suppose you have a string S which has length N and is indexed from 0 to N−1. String R is the reverse of the string S. The string S is funny if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.

(Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. |x| denotes the absolute value of an integer x)

Input Format
First line of the input will contain an integer T. T testcases follow. Each of the next T lines contains one string S.
'''

def funny_string():
    result = []
    num_cases = int(raw_input())
    for i in range(num_cases):
        result.append(is_funny(raw_input()))
    print "\n".join(result)

def is_funny(str):
    for letter in range(len(str)):
        left = abs(ord(str[letter]) - ord(str[letter - 1]))
        right = abs(ord((str[::-1])[letter]) - ord((str[::-1])[letter - 1]))
        if left != right:
            return "Not Funny"
    return "Funny"

funny_string()
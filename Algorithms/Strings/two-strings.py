'''
Problem Statement
You are given two strings, A and B. Find if there is a substring that appears in both A and B.

Input Format
Several test cases will be given to you in a single file. The first line of the input will contain a single integer T, the number of test cases.

Then there will be T descriptions of the test cases. Each description contains two lines. The first line contains the string A and the second line contains the string B.
'''

def two_strings():
    num_cases = int(raw_input())
    result = []
    for case in range(num_cases):
        strA = set(raw_input())
        strB = set(raw_input())
        if set.intersection(strA,strB):
            result.append("YES")
        else:
            result.append("NO")
    print "\n".join(result)

two_strings()
'''
Problem Statement
Given a list containing N integers, calculate the XorSum of all the non-empty subsets of the list and print the value of XorSum % (109+7).

XOR operation on a list is defined as the xor, of all the elements present in it, e.g.,
XOR({A,B,C})=A+B+C.

Input Format
An integer T, denoting the number of testcases. 2*T lines follow.
Each testcase contains two lines, first line will contains an integer N followed by second line containing N integers, a1,a2,...,aN, separated by a single space.
'''

import itertools

#nota bene: this works except when the input sizes are >100 kb
def xoring_ninja():
    results = []
    num_cases = int(raw_input())
    for case in range(num_cases):
        num_nums = int(raw_input())
        digits = map(int, raw_input().split())
        combos = []
        for i in range(1, len(digits)+1):
            c = [list(x) for x in itertools.combinations(digits, i)]
            combos.extend(c)
        combos = [reduce(lambda x,y: x^y, x) for x in combos]
        results.append(str(reduce(lambda x,y: x+y, combos)))
    print "\n".join(results)

xoring_ninja()
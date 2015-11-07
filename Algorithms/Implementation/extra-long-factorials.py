'''
Problem Statement
You are given an integer N. Print the factorial of this number.
N!=N×(N−1)×(N−2)×⋯×3×2×1

Input
Input consists of a single integer N, where 1≤N≤100.
'''

def extra_long_factorials():
	num = int(raw_input())
	res = 1
	while(num >= 1):
		res = res * num
		num -= 1
	print res

extra_long_factorials()

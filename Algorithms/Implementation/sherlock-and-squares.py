'''
Watson gives two integers (A and B) to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.

Input Format
The first line contains T, the number of test cases. T test cases follow, each in a new line.
Each test case contains two space-separated integers denoting A and B.
'''

import math

def sherlock_and_squares():
	num_cases = int(input())
	squares = 0
	cases = []
	for case in range(num_cases):
		test = [int(x) for x in input().split()]
		cases.append(test)
	for x in range(len(cases)):
		print(math.floor(math.sqrt(cases[x][1])) - math.floor(math.sqrt(cases[x][0]-1)))

def is_square(x):
	x = x ** 0.5
	return int(x) == x

sherlock_and_squares()




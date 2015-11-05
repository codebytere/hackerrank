'''
Problem Statement
You are given an integer N. Find the digits in this number that exactly divide N (division that leaves 0 as remainder) and display their count. For N=24, there are 2 digits (2 & 4). Both of these digits exactly divide 24. So our answer is 2.

Input Format
The first line contains T (the number of test cases), followed by T lines (each containing an integer N).
'''

def find_digits():
	num_cases = input()
	results = []
	for i in range(num_cases):
			num = raw_input()
			count = 0
			for digit in num:
					if digit != '0' and int(num) % int(digit) == 0:
							count = count + 1
			results.append(str(count))
	print "\n".join(results)

find_digits()

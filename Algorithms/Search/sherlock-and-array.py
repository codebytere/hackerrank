'''
Problem Statement
Watson gives Sherlock an array A of length N. Then he asks him to determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero.
Formally, find an i, such that, A1+A2...Ai-1 =Ai+1+Ai+2...AN.

Input Format
The first line contains T, the number of test cases. For each test case, the first line contains N, the number of elements in the array A. The second line for each test case contains N space-separated integers, denoting the array A.
'''

def sherlock_and_array():
	num_cases = int(raw_input())
	for case in range(num_cases):
		array_len = int(raw_input())
		print even_partition(map(int, raw_input().split()))

def even_partition(arr):
	for i in range(len(arr)):
		left_sum = 0 if i == 0 else reduce(lambda x,y: x+y, arr[:i])
		right_sum = 0 if i == len(arr) - 1 else reduce(lambda x,y: x+y, arr[i+1:])
		if left_sum == right_sum:
			return "YES"
	return "NO"

sherlock_and_array()

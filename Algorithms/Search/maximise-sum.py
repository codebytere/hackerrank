'''
Problem Statement
You are given an array of size N and another integer M. Your target is to find the maximum value of sum of subarray modulo M.
Subarray is a continous subset of array elements.
Note that we need to find the maximum value of (Sum of Subarray)%M , where there are N*(N+1)/2 possible subarrays.

Input Format
First line contains T , number of test cases to follow. Each test case consists of exactly 2 lines. First line of each test case contain 2 space separated integers N and M, size of the array and modulo value M.
Second line contains N space separated integers representing the elements of the array.
'''

def maximise_sum():
	num_cases = int(raw_input())
	for case in range(num_cases):
		(arr_len, mod) = [int(x) for x in raw_input().split()]
		arr = map(int, raw_input().split())
		print get_max(arr, mod)

def get_max(arr, mod):
	max_sum = 0
	for i in range(len(arr)):
		for j in range(i+1, len(arr) + 1):
			s = sum(arr[i:j])%mod
			if s > max_sum:
				max_sum = s
	return max_sum

maximise_sum()

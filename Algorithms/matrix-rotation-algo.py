'''
Problem Statement
You are given a 2D matrix, a, of dimension MxN and a positive integer R. You have to rotate the matrix R times and print the resultant matrix. Rotation should be in anti-clockwise direction.
Rotation of a 4x5 matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only (refer sample tests for more clarity).
It is guaranteed that the minimum of M and N will be even.

Input
First line contains three space separated integers, M, N and R, where M is the number of rows, N is number of columns in matrix, and R is the number of times the matrix has to be rotated. Then M lines follow, where each line contains N space separated positive integers. These M lines represent the matrix.
'''

def rotate():
	matrix = []
	params = map(int, raw_input().split())
	M = params[0]
	N = params[1]
	num_rotations = params[2]

	for i in range(M):
		matrix.append(map(int, raw_input().split()))

	for i in range(num_rotations):
		rotated = list(reversed(zip(*matrix)))

	for row in rotated:
		print row

rotate()

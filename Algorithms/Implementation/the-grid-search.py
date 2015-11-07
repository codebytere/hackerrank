'''
Problem Statement
Given a 2D array of digits, try to find the location of a given 2D pattern of digits. If we scan through the original array, we observe that the 2D pattern begins at the second row and the third column of the larger grid (the 8 in the second row and third column of the larger grid is the top-left corner of the pattern we are searching for).

So, a 2D pattern of P digits is said to be present in a larger grid G, if the latter contains a contiguous, rectangular 2D grid of digits matching with the pattern P, similar to the example shown above.

Input Format
The first line contains an integer, T, which is the number of test cases. T test cases follow, each having a structure as described below:
The first line contains two space-separated integers, R and C, indicating the number of rows and columns in the grid G, respectively.
This is followed by R lines, each with a string of C digits, which represent the grid G.
The following line contains two tab-separated integers, r and c, indicating the number of rows and columns in the pattern grid P.
This is followed by r lines, each with a string of c digits, which represent the pattern P.
'''

def the_grid_search():
	num_cases = int(raw_input())
	result = []

	for case in range(num_cases):
		m_rows,m_cols = [int(x) for x in raw_input().split()]
		mtx = [raw_input() for x in range(m_rows)]

		sm_rows,sm_cols = [int(x) for x in raw_input().split()]
		sub_mtx = [raw_input() for x in range(sm_rows)]

		i = 0
		found = 0
		initial_index = 0
		while i < m_rows :
			res = mtx[i].find(sub_mtx[0])
			if res != -1:
				initial_index = mtx[i].index(sub_mtx[0])
				j = 0
				while j < sm_rows and res != -1 :
					res = mtx[i].find(sub_mtx[j])
					if res == -1 or mtx[i].index(sub_mtx[j]) != initial_index:
						res = -1
					i += 1
					j += 1

				if j == sm_rows and res != -1:
					found = 1
			i += 1

		result.append("YES") if found else result.append("NO")
	print "\n".join(result)

the_grid_search()

'''
Problem Statement
You are given a square map of size n×n. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side (edge).

You need to find all the cavities on the map and depict them with the uppercase character X.

Input Format
The first line contains an integer, n, denoting the size of the map. Each of the following n lines contains n positive digits without spaces. Each digit (1-9) denotes the depth of the appropriate area.
'''

def cavity_map():
	rows = int(raw_input())

	cav_map = []
	result = []

	for i in range(rows):
		cav_map.append(raw_input())
	result.append(cav_map[0])

	for i in range(1, len(cav_map) - 1):
		result.append(cav_map[i][0])
		for a in range(1, len(cav_map[i]) - 1):
			target,top,right,bottom,left = int(cav_map[i][a]),int(cav_map[i - 1][a]),int(cav_map[i][a + 1]),int(cav_map[i + 1][a]),int(cav_map[i][a - 1])
			if target > top and target > right and target > bottom and target > left:
				result[i] += "X"
			else:
				result[i] += cav_map[i][a]
		result[i] += cav_map[i][-1]

	if rows != 1:
		result.append(cav_map[-1])

	for i in range(len(result)):
		print(result[i])

cavity_map()

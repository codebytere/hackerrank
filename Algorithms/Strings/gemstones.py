'''
Problem Statement
John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lower-case Latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a gem-element if it occurs at least once in each of the rocks.

Given the list of N rocks with their compositions, display the number of gem-elements that exist in those rocks.

Input Format
The first line consists of an integer, N, the number of rocks.
Each of the next N lines contains a rock's composition. Each composition consists of lower-case letters of English alphabet.
'''

def gemstones():
		num_strings = int(raw_input())
		pool = set()
		for i in range(num_strings):
				string = raw_input()
				if(i == 0):
						pool = pool.union(list(string))
				else:
						pool = pool.intersection(list(string))
		print len(pool)

gemstones()

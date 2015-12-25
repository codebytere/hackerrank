'''
Problem Statement
Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either a or b. Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was 0, find all the possible values for the number on the last stone.
Note: The numbers on the stones are in increasing order.

Input Format
The first line contains an integer T, i.e. the number of test cases. T test cases follow; each has 3 lines. The first line contains n (the number of stones). The second line contains a, and the third line contains b.
'''

def print_last():
	num_cases = int(raw_input())
	res = []
	for case in range(num_cases):
		num_stones = int(raw_input())
		a = int(raw_input())
		b = int(raw_input())
		res.append(get_range(num_stones, a, b))
	for item in res:
		print " ".join(str(e) for e in item)

def get_range(num, a, b):
	return sorted(set([(num - i - 1) * a + i * b for i in range(num)]))

print_last()

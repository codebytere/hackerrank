'''
Problem Statement
Calvin is driving his favorite vehicle on the 101 freeway. He notices that the check engine light of his vehicle is on, and he wants to service it immediately to avoid any risks. Luckily, a service lane runs parallel to the highway. The length of the service lane is N units. The service lane consists of N segments of equal length and different width.

Calvin can enter to and exit from any segment. Let's call the entry segment as index i and the exit segment as index j. Assume that the exit segment lies after the entry segment i<j and 0<i. Calvin has to pass through all segments from index i to index j (both inclusive).

Input Format
The first line of input contains two integers, N and T, where N denotes the length of the freeway and T the number of test cases. The next line has N space-separated integers which represent the width array.

T test cases follow. Each test case contains two integers, i and j, where i is the index of the segment through which Calvin enters the service lane and j is the index of the lane segment through which he exits.
'''

def service_lane():
	params = map(int, raw_input().split())
	lanes = map(int, raw_input().split())
	lane_length = params[0]
	num_cases = params[1]
	results = []
	for segment in range(num_cases):
		a,b = raw_input().split()
		results.append(str(min(lanes[int(a):(int(b)+1)])))
	print "\n".join(results)

service_lane()

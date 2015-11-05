'''
Problem Statement
You are given a list of N people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not. Find out the maximum number of topics a 2-person team can know. And also find out how many teams can know that maximum number of topics.

Note Suppose a, b, and c are three different people, then (a,b) and (b,c) are counted as two different teams.

Input Format
The first line contains two integers, N and M, separated by a single space, where N represents the number of people, and M represents the number of topics. N lines follow.
Each line contains a binary string of length M. If the ith line's jth character is 1, then the ith person knows the jth topic; otherwise, he doesn't know the topic.
'''

def acm_icpc_team():
	num_people, num_topics = (int(x) for x in raw_input().split())
	people = [raw_input() for x in range(num_people)]

	max_topics = 0
	max_teams = 0

	for row, p1 in enumerate(people):
		for col, p2 in enumerate(people[row+1:]):
				a,b = int(p1, 2),int(p2, 2)
				topics = bin(a | b).count('1')

				if topics > max_topics:
						max_topics = topics
						max_teams = 1
				elif topics == max_topics:
						max_teams += 1

	print max_topics
	print max_teams

acm_icpc_team()

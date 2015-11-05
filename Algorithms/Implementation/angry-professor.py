'''
Problem Statement
The professor is conducting a course on Discrete Mathematics to a class of N students. He is angry at the lack of their discipline, and he decides to cancel the class if there are fewer than K students present after the class starts.Given the arrival time of each student, your task is to find out if the class gets cancelled or not.

Input Format
The first line of the input contains T, the number of test cases. Each test case contains two lines.The first line of each test case contains two space-separated integers, N and K.
The next line contains N space-separated integers representing the arrival time of each student.If the arrival time of a given student is a non-positive integer, then the student enters before the class starts. If the arrival time of a given student is a positive integer, the student enters after the class has started.
'''

def class_cancelled():
	ans = []
	num_cases = int(raw_input())

	for i in range(num_cases):
		min_students = map(int, raw_input().split())[1]
		student_times = map(int, raw_input().split())
		on_time_students = filter(lambda x: x <= 0, student_times)

		result = "YES" if len(on_time_students) < min_students else "NO"
		ans.append(result)

	for answer in ans:
		print answer

class_cancelled()

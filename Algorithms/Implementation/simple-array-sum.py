'''
Problem Statement
You are given an array of integers of size N. Can you find the sum of the elements in the array?

Input:
The first line of input consists of an integer N. The next line contains N space-separated integers representing the array elements.
'''

size = int(raw_input())
arr = map(int, raw_input().split())

print reduce(lambda x,y: x+y, arr)

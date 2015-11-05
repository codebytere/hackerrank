'''
Problem Statement
You are given N sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.
Suppose we have six sticks of the following lengths: 5 4 4 2 2 8
Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following: 3 2 2 6
The above step is repeated until no sticks are left.
Given the length of N sticks, print the number of sticks that are left before each subsequent cut operations.

Input Format
The first line contains a single integer N.
The next line contains N integers: a0, a1,...aN-1 separated by space, where ai represents the length of ith stick.
'''

import sys
import collections

def cut_the_sticks():
		num_cuts = int(sys.stdin.readline())
		sticks = collections.Counter(map(int, sys.stdin.readline().split()))

		for stick in sorted(sticks):
				print(num_cuts)
				num_cuts -= sticks[stick]

cut_the_sticks()

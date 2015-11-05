'''
Problem Statement
The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. You are given the actual and the expected return dates. Calculate the fine as follows:

If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
If the book is returned in the same calendar month as the expected return date, Fine = 15 Hackos * Number of late days
If the book is not returned in the same calendar month but in the same calendar year as the expected return date, Fine = 500 Hackos * Number of late months
If the book is not returned in the same calendar year, the fine is fixed at 10000 Hackos.

Input
You are given the actual and the expected return dates in D M Y format in two separate lines. The first line contains the D M Y values for the actual return date and the next line contains the D M Y values for the expected return date. Here's a sample:
'''
def library_fine():
	actual = map(int, raw_input().split())
	expected = map(int, raw_input().split())

	yDiff = actual[2]-expected[2]
	mDiff = actual[1]-expected[1]
	dDiff = actual[0]-expected[0]

	if(yDiff >= 1):
		print 10000
	elif(yDiff < 0):
		print 0
	else:
		if(mDiff >= 1):
			print 500*mDiff
		elif (mDiff < 0):
			print 0
		else:
			if(dDiff >= 1):
				print 15*dDiff
			else:
				print 0

library_fine()


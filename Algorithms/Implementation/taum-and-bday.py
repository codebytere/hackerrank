'''
Problem Statement
Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy B number of black gifts and W number of white gifts.

The cost of each black gift is X units.
The cost of every white gift is Y units.
The cost of converting each black gift into white gift or vice versa is Z units.
Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

Input Format
The first line will contain an integer T which will be the number of test cases.
There will be T pairs of lines. The first line of each test case will contain the values of integers B and W. Another line of each test case will contain the values of integers X, Y, and Z.
'''

def taum_and_bday():
	result = []
	num_cases = int(raw_input())
	for i in range(num_cases):
		(white,black) = [int(x) for x in raw_input().split()]
		(w_p,b_p,c_p) = [int(x) for x in raw_input().split()]

		w_c = white*w_p
		b_c = black*b_p

		min1 = min(b_c, black*(w_p + c_p))
		min2 = min(w_c, white*(b_p + c_p))

		result.append(str(min1+min2))
	print "\n".join(result)

taum_and_bday()
